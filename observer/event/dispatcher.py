from abstract_observer import Observer

class EventDispatcher:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type: str, observer: Observer):
        self._subscribers.setdefault(event_type, []).append(observer)

    def unsubscribe(self, event_type: str, observer: Observer):
        self._subscribers[event_type].remove(observer)

    def dispatch(self, event_type: str, payload: dict):
        for observer in self._subscribers.get(event_type, []):
            observer.update(payload)
            
