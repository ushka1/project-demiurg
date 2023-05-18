from dataclasses import dataclass, field
from typing import Dict


@ dataclass
class _Metadata:
    title: str
    author: str
    description: str


@dataclass
class _Exit:
    location_id: str
    text: str


@dataclass
class _Location:
    name: str
    text: str
    exits: Dict[str, _Exit] = field(default_factory=dict)

    def __post_init__(self):
        exits = {}
        for direction, exit in self.exits.items():
            if (isinstance(exit, dict)):
                exits[direction] = _Exit(**exit)
        self.exits = exits


@dataclass
class _Map:
    start_location_id: str
    end_location_id: str
    locations: Dict[str, _Location] = field(default_factory=dict)

    def __post_init__(self):
        updated_locations = {}
        for key, location in self.locations.items():
            if (isinstance(location, dict)):
                updated_locations[key] = _Location(**location)
        self.locations = updated_locations


@ dataclass
class GameData:
    metadata: _Metadata
    map: _Map

    def __post_init__(self):
        if (isinstance(self.metadata, dict)):
            self.metadata = _Metadata(**self.metadata)
        if (isinstance(self.map, dict)):
            self.map = _Map(**self.map)

    def get_location_by_id(self, location_id: str) -> _Location:
        return self.map.locations[location_id]
