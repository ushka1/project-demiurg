from kivy.app import App
from kivy.graphics import Color
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# from widgets.connection import ItemConfirm, Connection
# from widgets.drag_card import DragCard
from ui_library.widgets.game_card import GameCard

Builder.load_file('ui_library/screens/game_selection_screen.kv')


class GameSelectionScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app = App.get_running_app()

    def on_enter(self, *args):
        self.reload_games()

    def add_game_cards(self):
        games = self.app.get_available_games()

        for game in games:
            card = GameCard(game_title=game)
            self.ids.stack.add_widget(card)

    def handle_keyboard(self, key):
        pass

    def reload_games(self):
        to_remove = []
        for child in self.ids.stack.children:
            to_remove.append(child)

        for card in to_remove:
            self.ids.stack.remove_widget(card)

        self.add_game_cards()
