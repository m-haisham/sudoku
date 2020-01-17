from kivy.core.window import Window, Keyboard
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector

from core import Colors
from logic import DepthFirst, Blink
from logic.checker import Checker
from .subgrid import SubGrid
from .key import Number


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

        self.rows = 3
        self.cols = 3

        self.spacing = 2

        self.selected = None

        self.grid = []
        self.block = {}
        self.row = {}
        self.col = {}

        self.depth_first = DepthFirst(self.grid, self.block, self.row, self.col, dramatic=True)
        self.depth_first.setDaemon(True)

        Window.bind(on_key_up=self._on_key_up)

        for i in range(self.rows * self.cols):
            subgrid = SubGrid(callback=self.callback)

            block = [i % self.cols, int(i / 3)]
            self.block[tuple(block)] = []

            for tile in subgrid.children:
                tile.block = block
                self.block[tuple(block)].append(tile)

            self.add_widget(subgrid)

        # initialization
        for i in range(9):
            self.grid.append([None] * 9)

            self.row[i] = []
            self.col[i] = []

        # grid fill and data identification
        for subgrid_no, subgrid in enumerate(self.children):

            block = Vector(subgrid_no % 3, int(subgrid_no / 3))
            for tile_no, tile in enumerate(subgrid.children):
                x = int(tile_no / 3) + block.y * 3
                y = tile_no % 3 + block.x * 3

                # flips
                x = (x * -1) + (9 - 1)
                y = (y * -1) + (9 - 1)

                tile.coords = [x, y]

                self.row[x].append(tile)
                self.col[y].append(tile)

                self.grid[x][y] = tile

    def _on_key_up(self, instance, keycode, scancode):
        number = Number.mapper(keycode)
        if number is not None:

            if self.selected is not None:
                self.selected.review = number

            return False

        elif keycode == 13 or keycode == 271:  # enter
            tile = self.selected

            checkings = set(self.block[tuple(tile.block)] + self.row[tile.coords[0]] + self.col[tile.coords[1]])
            repeats = Checker.specific(checkings, smart=True)
            if repeats:
                for tile in repeats:
                    Blink(tile, Colors.lerp((tile.review + 1) / 12, Colors.RED, Colors.WHITE).rgba).start()
                return

            tile.current, tile.review = tile.review, 0

            for tile in checkings:
                if tile.current != 0 or tile.review != 0:
                    Blink(tile, Colors.GREEN.rgba, 0.5).start()

        elif keycode == 32:  # spacebar
            self.depth_first.start()

    def callback(self, instance):
        # self.grid[0][0].current = 3
        # self.grid[0][0].selectable = False
        # self.depth_first.start()
        # return
        if not instance.selectable:
            return

        if self.selected is not None:
            self.selected.selected = False

        instance.selected = True
        self.selected = instance

    @staticmethod
    def print_grid(grid, key=None):
        if key is None:
            key = lambda value: value

        size = Vector(len(grid), len(grid[0]))
        for x in range(size.x):
            print('[', end='')
            for y in range(size.y):
                value = key(grid[x][y])
                print(value, end='')
                if y != size.y - 1:
                    print(', ', end='')
            print(']')
        print()
