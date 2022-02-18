import enum

from python.config.configurable import Configurable

class Keybind(enum.Enum, Configurable):

    UP,
    DOWN,
    RIGHT,
    LEFT,
    FORWARD,
    BACKWARD,
    PLANNING,
    STOP,
    EMERGENCY
