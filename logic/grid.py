
class GridIterator:
    def __init__(self, grid, shift=0):
        self.grid = grid

        self.forward = True
        self.i = 0

        copy = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                copy.append(self.grid[x][y])

        self.tiles = copy[shift:]
        self.tiles += copy[:shift]

    def back(self):
        self.i -= 2
        self.forward = False

    def stay(self):
        self.i -= 1

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.tiles):
            raise StopIteration

        if self.forward:
            while True:
                if self.i >= len(self.tiles):
                    raise StopIteration

                tile = self.tiles[self.i]
                if tile.selectable:
                    break

                self.i += 1

            self.i += 1
            return tile
        else:
            while True:
                if self.i < 0:
                    raise StopIteration

                tile = self.tiles[self.i]
                if tile.selectable:
                    break

                self.i -= 1

            self.forward = True
            self.i += 1
            return tile

