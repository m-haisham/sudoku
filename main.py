from kivy import Config
from kivy.app import App

from core import Navigation
from widgets.menu import Menu
from widgets.screen import SudokuScreen

Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')


class SudokuApp(App):
    navigation = Navigation.manager()

    def __init__(self, **kwargs):
        super(SudokuApp, self).__init__(**kwargs)

    def build(self):
        menu = Menu()
        self.navigation.add_widget(menu)
        self.navigation.add_widget(SudokuScreen())

        menu.init()

        return self.navigation


if __name__ == '__main__':
    SudokuApp().run()
