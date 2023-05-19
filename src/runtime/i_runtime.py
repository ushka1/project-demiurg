from abc import ABC, abstractmethod
from typing import Dict

from models.game_data import Exit, Location


class IRuntime(ABC):
    @abstractmethod
    def get_current_location(self) -> Location:
        pass

    @abstractmethod
    def get_available_exits(self) -> Dict[str, Exit]:
        pass

    @abstractmethod
    def get_message(self) -> str | None:
        pass

    @abstractmethod
    def select_exit(self, exit_id: str):
        pass
