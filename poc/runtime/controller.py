from models.game_data import GameData
from models.game_state import GameState, GameStateUpdate
from runtime.runtime_interface import RuntimeInterface


class Controller:
    def __init__(self,
                 runtime: RuntimeInterface,
                 game_data: GameData,
                 game_state: GameState):
        self.runtime = runtime
        self.game_data = game_data
        self.game_state = game_state

    def receive_update(self, game_state_update: GameStateUpdate):
        if (game_state_update.location):
            self.game_state.location = game_state_update.location

        self.runtime.notify_ui(self.game_state)
