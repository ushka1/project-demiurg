from dataclasses import dataclass
from typing import Dict, List

from config.globals import ui_type
from library.i_library import ILibrary
from models.game_data import GameData
from models.game_progress import GameProgress, QuestProgress
from models.map import Location, LocationExit
from models.quests import QuestStage
from runtime.i_runtime import IRuntime
from ui_console.ui_console import UIConsole

if ui_type == "kivy":
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

    def __init__(self,  game_data: GameData, game_progress: GameProgress, library: ILibrary):
        self.library = library

        if ui_type == "kivy":
            self.ui = GameUI(self)
            self.game_data = game_data
            self.game_progress = game_progress
            self.ui.run()

        if ui_type == "console":
            self.ui = UIConsole(self)
            self.game_data = game_data
            self.game_progress = game_progress
            self.update_ui()

    # =============== CONTROLS ===============

    def update_ui(self):
        self.ui.rerender()

    def save_game(self):
        self.library.save_game_progress(
            self.game_data.metadata.title, self.game_progress)

    def reset_game(self):
        self.game_progress = GameProgress.create_default_progress(
            self.game_data)
        self.save_game()
        self.update_ui()

    # =============== PLAYER ===============

    def set_player_name(self, name: str):
        self.game_progress.player_name = name

    def get_player_name(self) -> str:
        return self.game_progress.player_name

    # =============== GET ===============

    def get_current_location(self) -> Location:
        current_location = self.game_data.get_location_by_id(
            self.game_progress.location_id)
        return current_location

    def get_available_exits(self) -> Dict[str, LocationExit]:
        current_location = self.get_current_location()
        available_exits = current_location.exits
        return available_exits

    def get_available_quest_stages(self) -> List[QuestStage]:
        current_location_id = self.game_progress.location_id
        available_quest_stages = []

        for quest in self.game_data.quests.values():
            current_stage_id = quest.start_stage_id
            if self.game_progress.quests.get(quest.id):
                current_stage_id = self.game_progress.quests[quest.id].stage_id

            if quest.stages[current_stage_id].location_id == current_location_id:
                available_quest_stages.append(quest.stages[current_stage_id])

        return available_quest_stages

    def get_message(self) -> str | None:
        return self.game_progress.message

    # =============== SELECT ===============

    def select_exit(self, exit_key: str):
        available_exits = self.get_available_exits()

        if exit_key not in available_exits.keys():
            self.game_progress.message = "Invalid exit selected: " + exit_key
        else:
            self.game_progress.message = None
            self.game_progress.location_id = available_exits[exit_key].location_id

        self.update_ui()

    def select_quest_stage_option(self, quest_id: str, stage_id: str, option_id: str):
        try:
            option = self.game_data.quests[quest_id].stages[stage_id].options[option_id]

            if self.game_progress.quests.get(quest_id) is None:
                self.game_progress.quests[quest_id] = QuestProgress(
                    option.next_stage_id)
            else:
                self.game_progress.quests[quest_id].stage_id = option.next_stage_id

            self.game_progress.message = option.response_message

        except (KeyError, IndexError):
            self.game_progress.message = (f"Invalid option selected: "
                                          f"Quest={quest_id} Stage={stage_id} Option={option_id}")

        self.update_ui()
