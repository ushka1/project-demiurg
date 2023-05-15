from event_manager import EventManager
from ui import UI


class Game:
    def __init__(self):
        self.event_manager = EventManager()
        self.ui = UI(self.event_manager)
