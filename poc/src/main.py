import json
import os

from models.game_data import GameData
from models.game_state import GameState
from runtime.runtime import Runtime

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../library/mighty-roomba/game-data.json")

with open(file_path) as f:
    data_dict = json.load(f)

game_data = GameData(**data_dict)
game_state = GameState(location_id=game_data.map.start_location_id)
runtime = Runtime(game_data, game_state)

runtime.start()
