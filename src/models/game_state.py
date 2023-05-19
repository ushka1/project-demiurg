from dataclasses import dataclass


@dataclass
class GameState:
    location_id: str
    message: str | None = None
