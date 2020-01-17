import time
from threading import Thread

from core import Colors
from .checker import Checker
from .grid import GridIterator


class DepthFirst(Thread):
    def __init__(self, grid, blocks, rows, cols, dramatic=False, **kwargs):
        super(DepthFirst, self).__init__(**kwargs)

        self.grid = grid
        self.blocks = blocks
        self.rows = rows
        self.cols = cols

        self.dramatic = dramatic

        if dramatic:
            self.current_color = Colors.BLUE.rgba
            self.error_color = Colors.RED.rgba
        else:
            self.current_color = Colors.WHITE.rgba
            self.error_color = Colors.WHITE.rgba

    def _check(self, block, x, y):
        if self.dramatic:
            time.sleep(0.005)
        return Checker.tiles(self.blocks[tuple(block)]) and Checker.tiles(self.rows[x]) and Checker.tiles(self.cols[y])

    def run(self) -> None:

        grid_iterator = GridIterator(self.grid)

        for tile in iter(grid_iterator):
            tile.color = self.current_color

            if tile.current >= 9:
                tile.current = 0
                tile.color = self.error_color
                grid_iterator.back()
                continue

            tile.current += 1

            if not self._check(tile.block, tile.coords[0], tile.coords[1]):
                grid_iterator.stay()

            tile.color = Colors.WHITE.rgba

