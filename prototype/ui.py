from event_manager import EventManager


class UI:
    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager

    def setup(self):
        self.event_manager.subscribe(
            "update-location",
            self.update_location_handler)

    def update_location_handler(self, data):
        print(data)

    def print(self, message):
        print(message)

    def clear(self):
        print("--------------------")