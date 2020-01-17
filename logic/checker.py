
class Checker:

    @staticmethod
    def get_values(tiles, smart=False):
        values = []
        for tile in tiles:
            value = tile.current
            if smart and tile.review != 0:
                value = tile.review

            if value != 0:
                values.append(value)

        return values

    @staticmethod
    def tiles(tiles, smart=False):
        values = Checker.get_values(tiles, smart)

        return len(values) == len(set(values))

    @staticmethod
    def specific(tiles, smart=False):
        mapped = {}
        for tile in tiles:
            value = tile.current
            if smart and tile.review != 0:
                value = tile.review

            if value != 0:
                try:
                    mapped[value] += [tile]
                except KeyError:
                    mapped[value] = [tile]

        repeated = []
        for value in mapped.values():
            if len(value) > 1:
                repeated += value

        return repeated