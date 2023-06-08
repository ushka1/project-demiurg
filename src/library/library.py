import json
import os
from typing import Tuple

from models.game_data import GameData
from models.game_progress import GameProgress
from runtime.runtime import Runtime
from ui_library.library_ui import LibraryUI


class Library:
    current_folder = os.path.dirname(os.path.abspath(__file__))
    games_folder = os.path.join(
        current_folder,
        "../../games")

    def __init__(self):
        self.ui = LibraryUI(self)
        self.ui.run()

    def load_game(self, game_name: str) -> Tuple[GameData, GameProgress]:
        """
        Load the game data and game progress for the given game name. If
        progress does not exist, create a new one with default values.
        """
        game_data = self._load_game_data(game_name)

        try:
            game_progress = self._load_game_progress(game_name)
        except IOError:
            game_progress = GameProgress(
                location_id=game_data.map.start_location_id)

        return game_data, game_progress

    def _load_game_data(self, game_name: str) -> GameData:
        """
        Import content of game-data.json file and convert it into a GameData object.
        """
        game_data_path = os.path.join(
            self.games_folder,
            game_name,
            "game-data.json")

        with open(game_data_path) as f:
            json_data = json.load(f)

        return GameData(**json_data)

    def _load_game_progress(self, game_name: str) -> GameProgress:
        """
        Import content of game-progress.json file and convert it into a GameProgress object.
        """
        game_progress_path = os.path.join(
            self.games_folder,
            game_name,
            "game-state.json")

        with open(game_progress_path) as f:
            json_data = json.load(f)

        return GameProgress(**json_data)

    def get_available_games(self):
        """
        Get a list of all available games.
        """
        paths = [x[0] for x in os.walk(self.games_folder)]
        games = []

        for path in paths:
            game = path.replace(self.games_folder, "")
            game = game.replace("\\", "")
            game = game.replace("/", "")

            if game != "":
                games.append(game)

        return games

    def add_new_game(self, path: str) -> bool:
        """
        Add a new game to the library. The game must be a valid JSON file.
        """
        gamefile = open(path)
        data = json.load(gamefile)
        gamefile.close()

        title = data["metadata"]["title"]
        new_game_folder = os.path.join(self.games_folder, title)

        try:
            os.mkdir(new_game_folder)
        except FileExistsError:
            return False

        json_object = json.dumps(data, indent=4)
        json.dumps("")

        with open(os.path.join(new_game_folder, "game-data.json"), "w") as outfile:
            outfile.write(json_object)

        return True

    def run_game(self, game):
        """
        Run the game with the given name.
        """
        game_data, game_progress = self.load_game(game)
        self.ui.stop()

        runtime = Runtime(game_data, game_progress)
        runtime.start_game()
