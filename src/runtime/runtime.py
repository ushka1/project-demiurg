from dataclasses import dataclass
from typing import Dict

from models.game_data import Exit, GameData, Location
from models.game_progress import GameProgress
from runtime.i_runtime import IRuntime
from ui_game.game_ui import GameUI


@dataclass
class Runtime(IRuntime):
    """
    Runtime acts as a bridge between the UI and the game data. It is responsible for
    keeping track of the game progress and updating the UI when necessary.

    It also exposes some methods via the IRuntime interface that the UI can use to get
    information about the game progress (e.g. get_current_location) and
    to handle user actions (e.g. select_exit).
    """

    def __init__(self,  game_data: GameData, game_progress: GameProgress):
        self.ui = GameUI(self)
        self.game_data = game_data
        self.game_progress = game_progress
        self.ui.run()

    def start_game(self):
        return
        self.update_ui()

    def update_ui(self):
        self.ui.rerender()

    def get_current_location(self) -> Location:
        current_location = self.game_data.get_location_by_id(
            self.game_progress.location_id)
        return current_location

    def get_available_exits(self) -> Dict[str, Exit]:
        current_location = self.get_current_location()
        available_exits = current_location.exits
        return available_exits

    def get_message(self) -> str | None:
        return self.game_progress.message

    def select_exit(self, exit_key: str):
        available_exits = self.get_available_exits()

        if exit_key not in available_exits.keys():
            self.game_progress.message = "There is no exit: " + exit_key
        else:
            self.game_progress.message = None
            self.game_progress.location_id = available_exits[exit_key].location_id

        self.update_ui()

