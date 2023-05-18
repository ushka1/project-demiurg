from abc import ABC, abstractmethod

from models.game_state import GameState, GameStateUpdate


class IRuntime(ABC):
    @abstractmethod
    def notify_ui(self, game_state: GameState):
        pass

    @abstractmethod
    def notify_controller(self, game_state_update: GameStateUpdate):
        pass
