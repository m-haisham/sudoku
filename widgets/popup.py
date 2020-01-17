from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from core.layout import Column
from widgets.screen import reset_screens


class GridCheckPopup(Popup):
    def __init__(self, value):
        super(GridCheckPopup, self).__init__()

        self.size_hint = (0.5, 0.5)

        if value:
            self.title = 'Congratulations'

            self.content = Column()

            label = Label(text='You have found the solution')
            button = Button()
            button.text = 'MENU'
            button.size_hint = (0.5, 0.3)

            self.content.add_widget(label)
            self.content.add_widget(button)

        else:
            self.title = 'Try again'

            self.content = Column()

            label = Label(text='Your solution has a few flaws')
            button = Button()
            button.text = 'MENU'
            button.size_hint = (0.5, 0.3)

            self.content.add_widget(label)
            self.content.add_widget(button)

        button.bind(on_press=self.callback)

    def callback(self, instance):
        self.dismiss()
        reset_screens()

