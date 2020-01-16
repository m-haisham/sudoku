from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector

from .subgrid import SubGrid


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

        self.rows = 3
        self.cols = 3

        self.spacing = 2

        self.selected = None

        self.block = {}
        self.row = {}
        self.col = {}

        for i in range(self.rows * self.cols):
            subgrid = SubGrid(callback=self.callback)

            block = [i % self.cols, int(i / 3)]
            self.block[tuple(block)] = []

            for tile in subgrid.children:
                tile.block = block
                self.block[tuple(block)].append(tile)

            self.add_widget(subgrid)

        self.grid = []
        for i in range(9):
            self.grid.append([None] * 9)

            self.row[i] = []
            self.col[i] = []

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

    def callback(self, instance):
        if self.selected is not None:
            self.selected.selected = False

        instance.selected = True
        self.selected = instance

        instance.current, instance.review = instance.review, instance.current + 1
        if instance.current > 3:
            self.print_grid(self.grid, key=lambda value: value.current)

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
