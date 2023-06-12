from abc import ABC, abstractmethod
from typing import Dict, List

from models.map import Location, LocationExit
from models.quests import QuestStage


class IRuntime(ABC):
    """
    Interface for the runtime. This is the interface that the UI uses to
    communicate with the runtime.
    """

    # =============== CONTROLS ===============

    @abstractmethod
    def save_game(self) -> None:
        pass

    @abstractmethod
    def reset_game(self) -> None:
        pass

    # =============== PLAYER ===============

    @abstractmethod
    def set_player_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_player_name(self) -> str:
        pass

    # =============== GET ===============

    @abstractmethod
    def get_current_location(self) -> Location:
        pass

    @abstractmethod
    def get_available_exits(self) -> Dict[str, LocationExit]:
        pass

    @abstractmethod
    def get_available_quest_stages(self) -> List[QuestStage]:
        pass

    @abstractmethod
    def get_message(self) -> str | None:
        pass

    # =============== SELECT ===============

    @abstractmethod
    def select_exit(self, exit_id: str) -> None:
        pass

    @abstractmethod
    def select_quest_stage_option(self, quest_id: str, stage_id: str, option_id: str) -> None:
        pass
