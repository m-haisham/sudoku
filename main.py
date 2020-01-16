from random import randint

from kivy import Config
from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty, Clock, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from widgets import Grid


class SudokuApp(App):
    def __init__(self, **kwargs):
        super(SudokuApp, self).__init__(**kwargs)

    def build(self):
        return Grid()


if __name__ == '__main__':
    Config.set('graphics', 'width', '700')
    Config.set('graphics', 'height', '700')

    SudokuApp().run()
