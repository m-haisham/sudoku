from kivy.uix.gridlayout import GridLayout


class Row(GridLayout):
    def __init__(self, **kwargs):
        super(Row, self).__init__(**kwargs)

        self.rows = 1