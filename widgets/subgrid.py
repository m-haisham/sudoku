from kivy.uix.gridlayout import GridLayout

from .tile import GridTile


class SubGrid(GridLayout):
    def __init__(self, *, callback, **kwargs):
        super(SubGrid, self).__init__(**kwargs)

        self.rows = 3
        self.cols = 3

        for i in range(self.rows * self.cols):
            self.add_widget(GridTile(callback=callback))
