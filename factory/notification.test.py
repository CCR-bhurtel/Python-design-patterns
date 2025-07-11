import unittest
from notification import (
    NotifierFactory,
    EmailNotifier,
    SMSNotifier,
    PushNotifier,
)


class TestNotifierFactory(unittest.TestCase):

    def test_notifier_instances(self):
        test_cases = {
            "email": EmailNotifier,
            "sms": SMSNotifier,
            "push": PushNotifier,
        }

        for k, v in test_cases.items():
            notifier = NotifierFactory.create_notifier(k)
            self.assertIsInstance(notifier, v)


if __name__ == "__main__":
    unittest.main()
