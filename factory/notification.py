from abc import ABC, abstractmethod
import asyncio


_notifier_registry = {}


class Notifier(ABC):
    @abstractmethod
    async def send(self, message: str):
        pass


def register_notifier(name: str):
    def decorator(cls):
        _notifier_registry[name.lower()] = cls
        return cls

    return decorator


@register_notifier("sms")
class SMSNotifier(Notifier):
    def __init__(self, phone: str):
        self.phone = phone

    async def send(self, message: str):
        await asyncio.sleep()
        print(f"Sending SMS to {self.phone}: {message}")


@register_notifier("email")
class EmailNotifier(Notifier):
    def __init__(self, to: str):
        self.to = to

    async def send(self, message: str):
        await asyncio.sleep(1)
        print(f"Sending Email to {self.to}: {message}")


@register_notifier("push")
class PushNotifier(Notifier):
    def __init__(self, device_id: str):
        self.device_id = device_id

    async def send(self, message: str):
        await asyncio.sleep(1)
        print(f"Sending push notification to {self.device_id}: {message}")


# @register_notifier("whatsapp")
# class WhatsAppNotifier(Notifier):
#     def send(self, message: str):
#         print(f"Sending whatsapp message {message}")


class NotifierFactory:
    @staticmethod
    def create_notifier(notifier_type: str, **kwargs) -> Notifier:
        cls = _notifier_registry.get(notifier_type.lower())
        if not cls:
            raise ValueError(f"No notifier registered under name {notifier_type}")
        return cls(**kwargs)


async def main():
    notifier = NotifierFactory.create_notifier("push", device_id="12fdas")
    await notifier.send("Async message !")


asyncio.run(main())
