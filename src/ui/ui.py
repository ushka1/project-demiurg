import os
from dataclasses import dataclass

from runtime.i_runtime import IRuntime


@dataclass
class UI:
    """
    UI is responsible for rendering the game state and handling user input.
    """

    runtime: IRuntime

    def rerender(self):
        self.clear_terminal()

        current_location = self.runtime.get_current_location()
        print("Location: " + current_location.name)
        print(current_location.text)

        if current_location.is_end_location:
            return

        available_exits = self.runtime.get_available_exits()
        if available_exits:
            print("\nAvailable exits:")
            for key, value in available_exits.items():
                print(key + ": " + value.text)

        message = self.runtime.get_message()
        if message:
            print("\nMessage: " + message)

        self.listen_for_input()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def listen_for_input(self):
        exit_id = input("\nSelect exit: ")
        self.runtime.select_exit(exit_id)
