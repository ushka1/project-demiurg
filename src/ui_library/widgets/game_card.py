from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
import re

Builder.load_file('ui_library/widgets/game_card.kv')


class GameCard(MDCard):
    game_title = StringProperty("Game Title")
    game_author = StringProperty("Game Author")
    game_description = StringProperty("Game Description")
    game_tags: list

    def __init__(self, game_title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_title = game_title
        self.dialog = None

        details = App.get_running_app().library.get_game_details(self.game_title)
        self.game_author = details["author"]
        self.game_description = details["description"]
        self.game_tags = re.split(', |,', details["tags"])

    def show_open_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Do you want to play this game?",
                text=f"{self.game_title}\nby {self.game_author}\n\n{self.game_description}",
                buttons=[
                    MDFlatButton(
                        text="NEW GAME",
                        on_press=lambda x: self.play(force_reset=True),
                    ),
                    MDFlatButton(
                        text="LOAD",
                        on_press=lambda x: self.play(),
                    ),
                    MDFlatButton(
                        text="CANCEL",
                        on_press=lambda x: self.dismiss_dialog(),
                    ),
                ],
            )
        self.dialog.open()

    def show_delete_dialog(self):
        def delete():
            App.get_running_app().delete_game(self.game_title)
            self.dialog.dismiss()

        self.dialog = MDDialog(
            title="Delete project?",
            text="Warning: You cannot undo this action",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_press=lambda x: self.dismiss_dialog(),
                ),
                MDFlatButton(
                    text="DELETE",
                    on_press=lambda x: delete(),
                ),
            ],
        )
        self.dialog.open()

    def play(self, force_reset: bool = False):
        App.get_running_app().run_game(self.game_title, force_reset)

    def dismiss_dialog(self):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None
