import time
from threading import Thread

from core import Colors


class Blink(Thread):
    def __init__(self, tile, color, duration=0.3, **kwargs):
        super(Blink, self).__init__(**kwargs)

        self.tile = tile
        self.color = color
        self.duration = duration

        self.setDaemon(True)

    def run(self) -> None:
        self.tile.color = self.color
        time.sleep(self.duration)

        self.tile.set_color()