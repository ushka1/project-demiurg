from dataclasses import dataclass, field
from typing import Dict, Optional

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
class Exit:
    location_id: str
    text: str


@dataclass
class Location:
    name: str
    text: str
    exits: Dict[str, Exit] = field(default_factory=dict)
    is_end_location: Optional[bool] = None

    def __post_init__(self):
        exits = {}
        for direction, exit in self.exits.items():
            if (isinstance(exit, dict)):
                exits[direction] = Exit(**exit)
        self.exits = exits


@dataclass
class Map:
    start_location_id: str
    locations: Dict[str, Location] = field(default_factory=dict)

    def __post_init__(self):
        updated_locations = {}
        for key, location in self.locations.items():
            if (isinstance(location, dict)):
                updated_locations[key] = Location(**location)
        self.locations = updated_locations


@dataclass
class GameData:
    metadata: Metadata
    map: Map

    def __post_init__(self):
        if (isinstance(self.metadata, dict)):
            self.metadata = Metadata(**self.metadata)
        if (isinstance(self.map, dict)):
            self.map = Map(**self.map)

    def get_location_by_id(self, location_id: str) -> Location:
        return self.map.locations[location_id]
