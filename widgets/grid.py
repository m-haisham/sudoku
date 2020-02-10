from random import shuffle, randrange

from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector

from core import Colors
from logic import DepthFirst, Blink, Movement, GridCheck
from logic.checker import Checker
from .key import Number
from .subgrid import SubGrid


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

        self.depth_first = DepthFirst(self.grid, self.block, self.row, self.col, callback=self.reset_algorithm, dramatic=False)

        Window.bind(on_key_up=self._on_key_up, on_key_down=self._on_key_down)

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

        self.movement = Movement(self.grid)

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

    def reset_algorithm(self):
        self.depth_first = DepthFirst(self.grid, self.block, self.row, self.col, callback=self.reset_algorithm,
                                      dramatic=True)

    def _on_key_down(self, instance, keycode, scancode, *args):
        if keycode == 273 and self.selected is not None:  # up
            self.movement.up(self.selected.coords)
        elif keycode == 274 and self.selected is not None:  # down
            self.movement.down(self.selected.coords)
        elif keycode == 275 and self.selected is not None:  # right
            self.movement.right(self.selected.coords)
        elif keycode == 276 and self.selected is not None:  # left
            self.movement.left(self.selected.coords)

    def _on_key_up(self, instance, keycode, scancode):
        number = Number.mapper(keycode)
        if number is not None:

            if self.selected is not None:
                if self.selected.review == 0 and number == 0:
                    self.selected.current = 0

                self.selected.review = number

            return False

        elif keycode == 102 and self.selected is not None:  # f
            if self.selected.current == 0:
                Blink(self.selected, Colors.RED.rgba, 0.1).start()
                return

            self.selected.selected = False
            self.selected.selectable = not self.selected.selectable

        elif keycode == 99:
            def _callback(value):
                from .popup import GridCheckPopup
                GridCheckPopup(value).open()

            GridCheck(self.block, self.row, self.col, callback=_callback, dramatic=True).start()

        elif keycode == 13 or keycode == 271:  # enter
            tile = self.selected

            block = self.block[tuple(tile.block)]
            row = self.row[tile.coords[0]]
            col = self.col[tile.coords[1]]

            repeats = Checker.specific(block, smart=True)
            repeats += Checker.specific(row, smart=True)
            repeats += Checker.specific(col, smart=True)

            if repeats:
                for tile in repeats:
                    Blink(tile, Colors.lerp((tile.review + 1) / 10, Colors.WHITE, Colors.RED).rgba).start()
                return

            if tile.review != 0:
                tile.current, tile.review = tile.review, 0

            for tile in block + row + col:
                if tile.current != 0 or tile.review != 0:
                    Blink(tile, Colors.GREEN.rgba, 0.5).start()

        elif keycode == 32:  # spacebar
            self.depth_first.start()

    def random(self, percentile, callback):
        def _callback():

            tiles = []
            for x in range(len(self.grid)):
                for y in range(len(self.grid[0])):
                    tiles.append(self.grid[x][y])

            l = list(range(81))

            shuffle(l)

            for i in l[:amount]:
                tile = tiles[i]
                tile.selectable = False

            for i in l[amount:]:
                tile = tiles[i]
                tile.current = 0

            self.depth_first = DepthFirst(self.grid, self.block, self.row, self.col, callback=self.reset_algorithm, dramatic=True)
            callback()

        amount = int(percentile * 81)
        self.depth_first.shift = randrange(81)
        self.depth_first.callback = _callback
        self.depth_first.start()

    def callback(self, instance):
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
