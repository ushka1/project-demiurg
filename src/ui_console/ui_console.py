import os
from dataclasses import dataclass

from runtime.i_runtime import IRuntime


@dataclass
class UIConsole:
    """
    UI is responsible for rendering the game state and handling user input.
    """

    runtime: IRuntime

    def rerender(self):
        self.clear_terminal()
        self.render_location()
        self.render_message()

        if self.runtime.get_current_location().is_end_location:
            # end of game
            return

        self.render_quest_stages()
        self.render_exits()

        self.listen_for_input()

    def render_exits(self):
        available_exits = self.runtime.get_available_exits()
        if available_exits:
            print("\nAvailable exits:")
            for key, value in available_exits.items():
                print(key + ": " + value.text)

    def render_location(self):
        current_location = self.runtime.get_current_location()
        print("Location: " + current_location.name)
        print(current_location.text)

    def render_quest_stages(self):
        available_quest_stages = self.runtime.get_available_quest_stages()
        if available_quest_stages:
            for quest_stage in available_quest_stages:
                print(f"\nQuest {quest_stage.quest.id} "
                      f"Stage {quest_stage.id}: {quest_stage.quest.name}")
                print(quest_stage.text)

                for option in quest_stage.options.values():
                    print(f"Option {option.id}: " + option.text)

    def render_message(self):
        message = self.runtime.get_message()
        if message:
            print("\nMessage: " + message)

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def listen_for_input(self):
        choice = input("\nYour choice: ").upper()

        try:
            if choice == "QUIT":
                return

            if choice == "RESET":
                return self.runtime.reset_game()

            if choice.startswith("E"):
                exit_id = choice.split(" ")[1]
                return self.runtime.select_exit(exit_id)

            if choice.startswith("Q"):
                quest_id = choice.split(" ")[1]
                stage_id = choice.split(" ")[2]
                option_id = choice.split(" ")[3]

                return self.runtime.select_quest_stage_option(
                    quest_id, stage_id, option_id)

        except Exception as e:
            print(e)

        print(f"Invalid input: {choice}")
        self.listen_for_input()
