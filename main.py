from kivy import Config
from kivy.app import App

from widgets import Grid

Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '700')


class SudokuApp(App):
    def __init__(self, **kwargs):
        super(SudokuApp, self).__init__(**kwargs)

    def build(self):
        return Grid()


if __name__ == '__main__':
    SudokuApp().run()
