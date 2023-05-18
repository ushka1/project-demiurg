from models.game_data import GameData
from models.game_state import GameState, GameStateUpdate
from runtime.controller import Controller
from runtime.i_runtime import IRuntime
from runtime.ui import UI


class Runtime(IRuntime):
    def __init__(self,  game_data: GameData, game_state: GameState):
        self.ui = UI(self, game_data)
        self.controller = Controller(self, game_data, game_state)

    def notify_ui(self, game_state: GameState):
        self.ui.render(game_state)

    def notify_controller(self, game_state_update: GameStateUpdate):
        self.controller.receive_update(game_state_update)

    def start(self):
        self.notify_controller(GameStateUpdate())
