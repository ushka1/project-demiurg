from eventing import EventManager
from game_data import GameData
from map_controller import MapController
from ui import UI


class GameSession:
    def __init__(self, game_data: GameData):
        self.event_manager = EventManager()
        self.ui = UI(self.event_manager)
        self.map_controller = MapController(self.event_manager)

    def start(self):
        print("Game started!")

    def pause(self):
        print("Game paused!")
