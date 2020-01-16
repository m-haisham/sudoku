from kivy.lang import builder
from kivy.properties import BoundedNumericProperty, ColorProperty, NumericProperty, ObjectProperty, BooleanProperty, ListProperty
from kivy.uix.widget import Widget

from core import Colors


class GridTile(Widget):
    review = BoundedNumericProperty(0, min=0, max=9)
    current = BoundedNumericProperty(0, min=0, max=9)
    color = ColorProperty(Colors.WHITE.rgba)

    selected = BooleanProperty(False)

    border_color = ColorProperty(Colors.RED.rgba)
    border_width = NumericProperty(1)
    button = ObjectProperty(None)

    coods = ListProperty(None)
    block = ListProperty(None)

    def __init__(self, *, callback, **kwargs):
        super(GridTile, self).__init__(**kwargs)

        # self.current = randrange(0, 10)

        self.button.bind(on_press=lambda instance: callback(self))
