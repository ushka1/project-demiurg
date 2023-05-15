from event_manager import EventManager


class MapController:
    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager

    def setup(self):
        self.event_manager.subscribe(
            "update-location",
            self.update_location_handler)
