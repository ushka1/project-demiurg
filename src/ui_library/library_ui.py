import os
from dataclasses import dataclass

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from ui_library.screens.main_screen import MainScreen
from ui_library.screens.game_selection_screen import GameSelectionScreen


@dataclass
class LibraryUI(MDApp):
    """
    UI is responsible for rendering the game state and handling user input.
    """

    library: 'Library'
    screen_manager = ObjectProperty()

    def __init__(self, library, **kwargs):
        super().__init__(**kwargs)
        self.library = library

        LabelBase.register(name='Monoton', fn_regular='ui_game/assets/Monoton-Regular.ttf')
        LabelBase.register(name='Nunito', fn_regular='ui_game/assets/Nunito-VariableFont_wght.ttf')
        LabelBase.register(name='Nunito_bold', fn_regular='ui_game/assets/Nunito-Bold.ttf')
        LabelBase.register(name='Source_code_pro', fn_regular='ui_game/assets/SourceCodePro.ttf')
        LabelBase.register(name='Source_code_pro_bold', fn_regular='ui_game/assets/SourceCodePro-Bold.ttf')

        # Window.fullscreen = 'auto'

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.theme_style = "Dark"

    def get_available_games(self) -> list:
        return self.library.get_available_games()

    def run_game(self, game: str):
        self.library.run_game(game)


class NavigationButton(MDCard):
    text = StringProperty()