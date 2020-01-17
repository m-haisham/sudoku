from kivy.uix.button import Button
from kivy.vector import Vector


def CallResult(func):
    def wrapper(self, pos):
        r = func(self, Vector(pos[0], pos[1]))
        if r is None:
            return

        r.button.trigger_action()

    return wrapper