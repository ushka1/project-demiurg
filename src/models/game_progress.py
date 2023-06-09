from dataclasses import dataclass

"""
These are the dataclasses that represent the game progress. They are used to
convert the JSON data into Python objects for easier usage.
"""


@dataclass
class GameProgress:
    location_id: str
    message: str | None = None
