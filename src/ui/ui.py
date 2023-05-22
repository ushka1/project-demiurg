import os
from dataclasses import dataclass

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from ui.screens.game_screen import GameScreen
# from screens.creator_screen import CreatorScreen

from runtime.i_runtime import IRuntime


@dataclass
class UI(MDApp):
    """
    UI is responsible for rendering the game state and handling user input.
    """

    runtime: IRuntime
    screen_manager = ObjectProperty()

    def __init__(self, runtime, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.runtime = runtime

        LabelBase.register(name='Monoton', fn_regular='ui/assets/Monoton-Regular.ttf')
        LabelBase.register(name='Nunito', fn_regular='ui/assets/Nunito-VariableFont_wght.ttf')
        LabelBase.register(name='Nunito_bold', fn_regular='ui/assets/Nunito-Bold.ttf')
        LabelBase.register(name='Source_code_pro', fn_regular='ui/assets/SourceCodePro.ttf')
        LabelBase.register(name='Source_code_pro_bold', fn_regular='ui/assets/SourceCodePro-Bold.ttf')

    def on_start(self):
        self.screen_manager = self.root.ids.screen_manager
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        # self.rerender()

    def hook_keyboard(self, window, key, *largs):
        print(key)

        self.screen_manager.current_screen.handle_keyboard(key)

        return True

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.theme_style = "Dark"

    def rerender(self):
        self.screen_manager.current_screen.rerender()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def listen_for_input(self):
        exit_id = self.root.ids.text_field.text
        self.runtime.select_exit(exit_id)


class NavigationButton(MDCard):
    text = StringProperty()
