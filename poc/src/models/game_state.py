from dataclasses import dataclass


@dataclass
class GameState:
    location: str


@dataclass
class GameStateUpdate:
    location: str | None = None
