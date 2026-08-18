# Day 8 Assignment: Polymorphism & Duck Typing
# ----------------------------------------------------------------------
# Instructions: Implement the message dispatchers below.
# Do not inherit from a shared base class. Use Duck Typing.
# Run 'python day8_test.py' to verify your solutions.

# ======================================================================
# Notification Channel Classes (Unrelated parents, same duck type)
# ======================================================================

class SmsSender:
    """
    Requirements:
    1. Implement 'send(self, message, recipient)' returning: "SMS to <recipient>: <message>".
    """
    # TODO: Implement SmsSender


class EmailSender:
    """
    Requirements:
    1. Implement 'send(self, message, recipient)' returning: "Email to <recipient>: <message>".
    """
    # TODO: Implement EmailSender


class SlackSender:
    """
    Requirements:
    1. Implement 'send(self, message, recipient)' returning: "Slack to <recipient>: <message>".
    """
    # TODO: Implement SlackSender


# ======================================================================
# Polymorphic Client Dispatcher
# ======================================================================
class NotificationDispatcher:
    """
    Requirements:
    1. Constructor should take a 'sender' object. This can be an instance of
       SmsSender, EmailSender, SlackSender, or any other class implementing 'send'.
    2. Store it in 'self.sender'.
    3. Implement 'dispatch(self, message, recipient)' which calls
       self.sender.send(message, recipient) and returns the string output.
    """
    def __init__(self, sender):
        # TODO: Store sender
        pass

    def dispatch(self, message, recipient):
        # TODO: Call send on the sender and return results
        pass
