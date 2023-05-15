import json

from models.game_data import GameData
from models.game_state import GameState
from runtime.runtime import Runtime

filename = "./library/mighty-roomba/game-data.json"
with open(filename) as f:
    data_dict = json.load(f)

game_data = GameData(**data_dict)
game_state = GameState(location=game_data.map.start)
runtime = Runtime(game_data, game_state)

runtime.start()
