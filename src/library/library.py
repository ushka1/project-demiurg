import json
import os
from typing import Tuple

from models.game_data import GameData
from models.game_progress import GameProgress
from ui_library.library_ui import LibraryUI
from runtime.runtime import Runtime


class Library:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    library_dir = os.path.join(
        current_dir,
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
            self.library_dir,
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
            self.library_dir,
            game_name,
            "game-state.json")

        with open(game_progress_path) as f:
            json_data = json.load(f)

        return GameProgress(**json_data)

    def get_available_games(self):
        return ["mighty-roomba", "ant's-adventure"]

    def run_game(self, game):
        game_data, game_progress = self.load_game(game)
        self.ui.stop()

        runtime = Runtime(game_data, game_progress)
        runtime.start_game()
