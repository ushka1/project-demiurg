from eventing import EventManager, EventType


class UI:
    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager

    def setup(self):
        self.event_manager.subscribe(
            EventType.MAP_LOCATION_CHANGED,
            self.update_location)

    def update_location(self, data):
        print(data)
