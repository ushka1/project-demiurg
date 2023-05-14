class EventManager:

    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type not in self.listeners:
            return
        self.listeners[event_type].remove(listener)

    def notify(self, event: str, data: dict):
        if event not in self.listeners:
            return
        for listener in self.listeners[event]:
            listener.update(event, data)
