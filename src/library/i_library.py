from abc import ABC, abstractmethod

from models.game_progress import GameProgress


class ILibrary(ABC):
    @abstractmethod
    def save_game_progress(self, game_name: str, game_progress: GameProgress) -> None:
        pass
