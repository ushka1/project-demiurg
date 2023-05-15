from dataclasses import dataclass, field
from typing import Dict, List, Literal, Optional


@dataclass
class _Exit:
    to: str
    text: str


@dataclass
class _Location:
    id: str
    name: str
    text: str
    exits: Dict[Literal["N", "E", "S", "W"],
                Optional[_Exit]] = field(default_factory=dict)

    def __post_init__(self):
        exits = {}
        for direction, exit in self.exits.items():
            if (isinstance(exit, dict)):
                exits[direction] = _Exit(**exit)
        self.exits = exits


@dataclass
class _Game:
    start_location_id: str
    end_location_id: str
    locations: List[_Location] = field(default_factory=list)

    def __post_init__(self):
        updated_locations = []
        for location in self.locations:
            if (isinstance(location, dict)):
                updated_locations.append(_Location(**location))
        self.locations = updated_locations


@dataclass
class GameData:
    title: str
    author: str
    description: str
    game: _Game

    def __post_init__(self):
        if (isinstance(self.game, dict)):
            self.game = _Game(**self.game)
