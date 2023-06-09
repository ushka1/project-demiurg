from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


Builder.load_file('ui_game/widgets/oldschool_button_game.kv')


class OldschoolButtonGame(MDCard):
    text = StringProperty()

