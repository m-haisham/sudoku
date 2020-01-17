from kivy.uix.gridlayout import GridLayout


class Column(GridLayout):
    def __init__(self, **kwargs):
        super(Column, self).__init__(**kwargs)

        self.cols = 1