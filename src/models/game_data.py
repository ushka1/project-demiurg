from dataclasses import dataclass
from typing import Dict

from models.map import Location, Map
from models.quests import Quest

"""
These are the dataclasses that represent the game data. They are used to
convert the JSON data into Python objects for easier usage.
"""


@dataclass
class Metadata:
    title: str
    author: str
    description: str


@dataclass
class GameData:
    metadata: Metadata
    map: Map
    quests: Dict[str, Quest]

    def __post_init__(self):
        if (isinstance(self.metadata, dict)):
            self.metadata = Metadata(**self.metadata)

        if (isinstance(self.map, dict)):
            self.map = Map(**self.map)

        updated_quests = {}
        for quest_id, quest in self.quests.items():
            if (isinstance(quest, dict)):
                updated_quests[quest_id] = Quest(id=quest_id, **quest)
        self.quests = updated_quests

    def get_location_by_id(self, location_id: str) -> Location:
        return self.map.locations[location_id]
