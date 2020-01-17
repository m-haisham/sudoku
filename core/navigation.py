from kivy.uix import screenmanager


class Navigation(screenmanager.ScreenManager):
    instance = None

    def __init__(self, **kwargs):
        super(Navigation, self).__init__(**kwargs)

    @staticmethod
    def manager():
        if Navigation.instance is None:
            Navigation.instance = Navigation()

        return Navigation.instance
