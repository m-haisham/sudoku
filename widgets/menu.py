from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from core import Navigation


class Menu(Screen):
    easy = ObjectProperty(None)
    medium = ObjectProperty(None)
    hard = ObjectProperty(None)
    exit = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.name = 'menu'

        self.grid = None

        self.easy.bind(on_press=lambda _: self._start(0.7))
        self.medium.bind(on_press=lambda _: self._start(0.5))
        self.hard.bind(on_press=lambda _: self._start(0.2))
        self.exit.bind(on_press=lambda _: App.get_running_app().stop())

    def init(self):
        self.grid = Navigation.manager().screens[1].grid

    def _start(self, value):
        self.easy.disabled = False
        self.medium.disabled = False
        self.hard.disabled = False

        self.grid.random(value, callback=self.open)

    def open(self):
        Navigation.manager().current = 'sudoku'