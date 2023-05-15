from models.game_data import GameData
from models.game_state import GameState, GameStateUpdate
from runtime.controller import Controller
from runtime.runtime_interface import RuntimeInterface
from runtime.ui import UI


class Runtime(RuntimeInterface):
    def __init__(self,  game_data: GameData, game_state: GameState):
        self.controller = Controller(self, game_data, game_state)
        self.ui = UI(self, game_data)

    def notify_controller(self, game_state_update: GameStateUpdate):
        self.controller.receive_update(game_state_update)

    def notify_ui(self, game_state: GameState):
        self.ui.render(game_state)

    def start(self):
        self.notify_controller(GameStateUpdate())
