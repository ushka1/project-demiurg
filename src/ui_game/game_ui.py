import os
from dataclasses import dataclass

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

from ui_game.screens.game_screen import GameScreen


# from screens.creator_screen import CreatorScreen

from runtime.i_runtime import IRuntime


@dataclass
class GameUI(MDApp):
    """
    UI is responsible for rendering the game state and handling user input.
    """

    runtime: IRuntime
    screen_manager = ObjectProperty()

    def __init__(self, runtime, **kwargs):
        super().__init__(**kwargs)
        self.runtime = runtime

        Window.fullscreen = 'auto'

    def on_start(self):
        self.screen_manager = self.root.ids.screen_manager
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        # self.rerender()

    def hook_keyboard(self, window, key, *largs):
        self.screen_manager.current_screen.handle_keyboard(key)

        return True

    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.theme_style = "Dark"

    def rerender(self):
        self.screen_manager.current_screen.rerender()

    def get_available_games(self) -> list:
        return self.runtime.get_available_games()

    def restart_game(self):
        return self.runtime.reset_game()


class NavigationButtonGame(MDCard):
    text = StringProperty()
