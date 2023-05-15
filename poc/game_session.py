from game_data import GameData
from game_state import GameState
from ui import UI


class GameSession:
    def __init__(self, game_data: GameData, game_state: GameState):
        self.game_data = game_data
        self.game_state = game_state
        self.ui = UI(game_data)

    def start(self):
        self.ui.render(self.game_state)

    def pause(self):
        print("Game paused!")

    def resume(self):
        print("Game resumed!")
