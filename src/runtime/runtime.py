from copy import deepcopy
from dataclasses import dataclass
from typing import Dict

from models.game_data import Exit, GameData, Location
from models.game_state import GameState
from runtime.i_runtime import IRuntime
from ui.ui import UI


@dataclass
class Runtime(IRuntime):
    def __init__(self,  game_data: GameData, game_state: GameState):
        self.ui = UI(self)
        self.game_data = game_data
        self.game_state = game_state

    def start(self):
        self.ui.rerender()

    def get_current_location(self) -> Location:
        current_location = self.game_data.get_location_by_id(
            self.game_state.location_id)
        return current_location

    def get_available_exits(self) -> Dict[str, Exit]:
        current_location = self.get_current_location()
        available_exits = current_location.exits
        return available_exits

    def get_message(self) -> str | None:
        return self.game_state.message

    def select_exit(self, exit_key: str):
        available_exits = self.get_available_exits()

        if (exit_key not in available_exits.keys()):
            self.game_state.message = "There is no exit: " + exit_key
        else:
            self.game_state.message = None
            self.game_state.location_id = available_exits[exit_key].location_id

        self.ui.rerender()
