import json
import os

from models.game_data import GameData
from models.game_state import GameState
from runtime.runtime import Runtime

script_dir = os.path.dirname(os.path.abspath(__file__))
library_dir = os.path.join(script_dir, "../library")
game_path = os.path.join(library_dir, "mighty-roomba/game-data.json")

with open(game_path) as f:
    data_dict = json.load(f)

game_data = GameData(**data_dict)
game_state = GameState(location_id=game_data.map.start_location_id)
runtime = Runtime(game_data, game_state)

runtime.start()
