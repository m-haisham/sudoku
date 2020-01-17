from kivy.lang import builder
from kivy.properties import BoundedNumericProperty, ColorProperty, NumericProperty, ObjectProperty, BooleanProperty, \
    ListProperty
from kivy.uix.widget import Widget

from core import Colors

import random


class GridTile(Widget):
    review = BoundedNumericProperty(0, min=0, max=9)
    current = BoundedNumericProperty(0, min=0, max=9)

    color = ColorProperty(Colors.WHITE.rgba)
    faded = ColorProperty(Colors.GREY.rgba)

    _selected = BooleanProperty(False)
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    border_color = ColorProperty(Colors.RED.rgba)
    border_width = NumericProperty(1)
    button = ObjectProperty(None)

    coods = ListProperty(None)
    block = ListProperty(None)

    def __init__(self, *, callback, **kwargs):
        super(GridTile, self).__init__(**kwargs)

        self.button.bind(on_press=lambda instance: callback(self))

    def on_selected(self, instance, value):
        if self.selectable:
            self._selected = value

    def on_selectable(self, instance, value):
        if value:
            self.color = Colors.WHITE.rgba
        else:
            self.color = Colors.GREY.rgba

    def set_color(self):
        if self.selectable:
            self.color = Colors.WHITE.rgba
        else:
            self.color = Colors.GREY.rgba
