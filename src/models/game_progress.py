from dataclasses import dataclass, field
from typing import Dict

from models.game_data import GameData

"""
These are the dataclasses that represent the game progress. They are used to
convert the JSON data into Python objects for easier usage.
"""


@dataclass
class QuestProgress:
    stage_id: str


@dataclass
class GameProgress:
    location_id: str
    quests: Dict[str, QuestProgress] = field(default_factory=dict)
    message: str | None = None
    player_name: str | None = None

    def __post_init__(self):
        print(self.quests)

        updated_quests = {}
        for quest_id, quest in self.quests.items():
            if (isinstance(quest, dict)):
                updated_quests[quest_id] = QuestProgress(**quest)
        self.quests = updated_quests

    @staticmethod
    def create_default_progress(game_data: GameData) -> "GameProgress":
        return GameProgress(location_id=game_data.map.start_location_id)
