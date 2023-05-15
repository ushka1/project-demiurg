from game_data import GameData
from game_state import GameState


class UI:
    def __init__(self, game_data: GameData):
        self.game_data = game_data

    def render(self, game_state: GameState):
        current_location = self.game_data.map.locations[game_state.location]
        if current_location is None:
            raise RuntimeError("Invalid location: " + game_state.location)

        print(current_location.name + ": " + current_location.text + "\n")

        available_exits = current_location.exits
        print("Available exits:")
        for key, value in available_exits.items():
            print(key + ": " + value.text)
        print()

        choice = input("Your choice: ")
        while (choice not in available_exits):
            choice = input("Invalid choice. Try again: ")
