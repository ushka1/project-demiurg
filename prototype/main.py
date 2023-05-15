import json

from game_data import GameData
from game_session import GameSession
from game_state import GameState

filename = "game.json"
with open(filename) as f:
    data_dict = json.load(f)

game_data = GameData(**data_dict)
game_session = GameSession(game_data)

state1 = GameState(location_id="location1")
state2 = GameState(location_id="location2")

print(state1)
print(state2)
