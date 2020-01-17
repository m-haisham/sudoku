from kivy.uix.screenmanager import Screen

from core import Navigation
from .grid import Grid
from .menu import Menu


class SudokuScreen(Screen):
    def __init__(self, **kwargs):
        super(SudokuScreen, self).__init__(**kwargs)

        self.name = 'sudoku'
        self.grid = Grid()
        self.add_widget(self.grid)


def reset_screens():
    nav = Navigation.manager()

    menu = Menu()
    nav.screens[0] = menu
    nav.screens[1] = SudokuScreen()

    menu.init()

    nav.current = 'menu'

