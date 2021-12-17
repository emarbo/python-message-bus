from lib.messages import MessageMeta
from lib.messages import Message


class CommandMeta(MessageMeta):
    """
    The Command metaclass
    """

    _commands: dict[str, "CommandMeta"] = {}

    def __new__(cls, name, bases, dic):
        # super checks NAME correctness and may assign a default
        command_cls = super().__new__(cls, name, bases, dic)
        cls._commands[command_cls.NAME] = command_cls
        return command_cls

    @classmethod
    def _clear(cls):
        """
        Resets internal state. For testing.
        """
        cls._commands = {}


class Command(Message, metaclass=CommandMeta):
    """
    The Command base class. To inherit and set the NAME.
    """
