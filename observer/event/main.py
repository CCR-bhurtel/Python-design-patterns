from dispatcher import EventDispatcher
from abstract_observer import Observer


class Logger(Observer):
    def update(self, payload):
        print(f"[Logger] {payload}")


class EmailAlert(Observer):
    def update(self, payload):
        print(f"[Email] Alert triggered for: {payload['user_id']}")


dispatcher = EventDispatcher()
dispatcher.subscribe("user.signup", Logger())
dispatcher.subscribe("user.signup", EmailAlert())

dispatcher.dispatch("user.signup", {"user_id": 42, "email": "user@example.com"})
