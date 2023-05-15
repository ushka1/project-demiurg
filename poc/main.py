import json

from game_data import GameData
from game_session import GameSession
from game_state import GameState

filename = "mighty-roomba.json"
with open(filename) as f:
    data_dict = json.load(f)

game_data = GameData(**data_dict)
game_state = GameState(location=game_data.map.start)
game_session = GameSession(game_data, game_state)

game_session.start()
