from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.app import App

from ui_library.widgets.main_screen_button import MainScreenButton

Builder.load_file('ui_library/screens/main_screen.kv')


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

        self.app.main_screen = self

    def handle_keyboard(self, key):
        pass
