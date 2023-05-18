from dataclasses import dataclass
from typing import Optional


@dataclass
class GameState:
    location_id: str


@dataclass
class GameStateUpdate:
    location_id: Optional[str] = None
