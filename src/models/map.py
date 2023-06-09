from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class LocationExit:
    location_id: str
    text: str


@dataclass
class Location:
    name: str
    text: str
    exits: Dict[str, LocationExit] = field(default_factory=dict)
    is_end_location: Optional[bool] = None

    def __post_init__(self):
        updated_exits = {}
        for direction, exit in self.exits.items():
            if (isinstance(exit, dict)):
                updated_exits[direction] = LocationExit(**exit)
        self.exits = updated_exits


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
