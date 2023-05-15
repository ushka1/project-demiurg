from eventing import EventManager, EventType


class MapController:
    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager

    def setup(self):
        self.event_manager.subscribe(
            EventType.LOCATION_BUTTON_CLICK,
            self.update_location_handler)

    def update_location_handler(self, data):
        print(data)
