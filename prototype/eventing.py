from enum import Enum
from typing import Callable, Dict


class EventType(Enum):
    LOCATION_BUTTON_CLICK = 1
    MAP_LOCATION_CHANGED = 2


class EventManager:
    def __init__(self):
        self.listeners: Dict[EventType, list[Callable]] = {}

    def subscribe(self, event_type: EventType, listener: Callable):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type: EventType, listener: Callable):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def notify(self, event_type: EventType, data=None):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)
