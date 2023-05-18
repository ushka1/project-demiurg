from models.game_data import GameData
from models.game_state import GameState, GameStateUpdate
from runtime.i_runtime import IRuntime


class UI:
    def __init__(self, runtime: IRuntime, game_data: GameData):
        self.runtime = runtime
        self.game_data = game_data

    def render(self, game_state: GameState):
        current_location = self.game_data.map.locations[game_state.location_id]
        if current_location is None:
            raise RuntimeError("Invalid location: " + game_state.location_id)

        print(current_location.name + ": " + current_location.text + "\n")

        available_exits = current_location.exits
        print("Available exits:")
        for key, value in available_exits.items():
            print(key + ": " + value.text)
        print()

        choice = input("Your choice: ")
        while (choice not in available_exits):
            choice = input("Invalid choice. Try again: ")

        new_location_id = available_exits[choice].location_id

        self.runtime.notify_controller(
            GameStateUpdate(location_id=new_location_id))
