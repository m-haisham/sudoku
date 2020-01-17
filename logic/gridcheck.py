import time
from threading import Thread

from core import Colors
from .blink import blink_all
from .checker import Checker


class GridCheck(Thread):
    def __init__(self, blocks, rows, cols, callback=None, dramatic=False, **kwargs):
        super(GridCheck, self).__init__(**kwargs)
        self.setDaemon(True)

        self.blocks = blocks
        self.rows = rows
        self.cols = cols

        self.dramatic = dramatic
        self.valid = True

        self.callback = callback

    def run(self) -> None:
        for block in self.blocks.values():
            invalid = Checker.specific(block, True)
            invalid += Checker.zeroes(block)

            if invalid:
                self.valid = False

            if self.dramatic:
                blink_all(invalid, Colors.RED.rgba, 0.3)
                blink_all([tile for tile in block if tile not in invalid], Colors.GREEN.rgba)
                time.sleep(0.05)

        if self.dramatic:
            time.sleep(0.2)

        for row in self.rows.values():
            invalid = Checker.specific(row, True)
            invalid += Checker.zeroes(row)

            if invalid:
                self.valid = False

            if self.dramatic:
                blink_all(invalid, Colors.RED.rgba, 0.3)
                blink_all([tile for tile in row if tile not in invalid], Colors.GREEN.rgba)
                time.sleep(0.05)

        if self.dramatic:
            time.sleep(0.2)

        for col in self.cols.values():
            invalid = Checker.specific(col, True)
            invalid += Checker.zeroes(col)

            if invalid:
                self.valid = False

            if self.dramatic:
                blink_all(invalid, Colors.RED.rgba, 0.3)
                blink_all([tile for tile in col if tile not in invalid], Colors.GREEN.rgba)
                time.sleep(0.05)

        if self.callback is not None:
            self.callback(self.valid)