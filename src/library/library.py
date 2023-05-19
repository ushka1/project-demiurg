import json
import os

from models.game_data import GameData
from models.game_state import GameState


class Library:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    library_dir = os.path.join(
        current_dir,
        "../../games")

    def get_game_data(self) -> GameData:
        return self.game_data

    def get_game_state(self) -> GameState:
        return self.game_state

    def load_game(self, game_name: str):
        self.game_name = game_name
        self._load_game_data()
        self._load_game_state()

    def _load_game_data(self):
        game_data_path = os.path.join(
            self.library_dir,
            self.game_name,
            "game-data.json")

        with open(game_data_path) as f:
            json_data = json.load(f)

        self.game_data = GameData(**json_data)

    def _load_game_state(self):
        try:
            game_state_path = os.path.join(
                self.library_dir,
                self.game_name,
                "game-state.json")

            with open(game_state_path) as f:
                json_data = json.load(f)

            self.game_state = GameState(**json_data)
        except IOError:
            self.game_state = GameState(
                location_id=self.game_data.map.start_location_id)
