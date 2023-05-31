from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.card import MDCard


Builder.load_file('ui_library/widgets/game_card.kv')


class GameCard(MDCard):
    game_title = StringProperty("Project Title")

    def __init__(self, game_title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_title = game_title
