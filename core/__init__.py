from kivy.graphics import Color

from .navigation import Navigation

class Colors:
    WHITE = Color(1, 1, 1, 1)
    BLACK = Color(0, 0, 0, 1)

    GREY = Color(.8, .8, .8, 1)

    RED = Color(1, 0, 0, 1)
    GREEN = Color(0, 1, 0, 1)
    BLUE = Color(0, 0, 1, 1)

    @staticmethod
    def lerp(value, *args):

        if value <= 0:
            return args[0]
        elif value >= 1:
            return args[-1]

        a = None
        b = None

        pos = 2
        neg = -2

        slice = 1 / (len(args) - 1)
        for i in range(len(args)):
            v = i * slice
            diff = value - v
            if diff == 0:
                return args[i]
            elif diff > 0:
                if diff < pos:
                    b = args[i]
                    pos = diff
            else:
                if diff > neg:
                    a = args[i]
                    neg = diff

        pvalue = pos / slice
        nvalue = 1 - pvalue

        return Color(
            a.r * pvalue + b.r * nvalue,
            a.g * pvalue + b.g * nvalue,
            a.b * pvalue + b.b * nvalue,
            1
        )
