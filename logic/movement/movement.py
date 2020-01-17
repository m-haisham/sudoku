from kivy.vector import Vector

from .decorator import CallResult


class Movement:
    def __init__(self, grid):
        self.grid = grid
        self.size = Vector(len(self.grid), len(self.grid[0]))

    @CallResult
    def down(self, pos: Vector):
        x = pos.x + 1
        while x < self.size.x:
            tile = self.grid[x][pos.y]
            if tile.selectable:
                return tile
            x += 1

    @CallResult
    def up(self, pos):
        x = pos.x - 1
        while x >= 0:
            tile = self.grid[x][pos.y]
            if tile.selectable:
                return tile
            x -= 1

    @CallResult
    def left(self, pos):
        y = pos.y - 1
        while y >= 0:
            tile = self.grid[pos.x][y]
            if tile.selectable:
                return tile
            y -= 1

    @CallResult
    def right(self, pos):
        y = pos.y + 1
        while y < self.size.y:
            tile = self.grid[pos.x][y]
            if tile.selectable:
                return tile
            y += 1
