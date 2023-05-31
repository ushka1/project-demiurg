from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

Builder.load_file('ui_game/widgets/input_label.kv')


class InputLabel(MDCard):
    text = StringProperty()
    direction: str
    index: int

    def set_active_background(self):
        self.md_bg_color = (0, 0.6, 0.6, 1)

    def reset_background(self):
        self.md_bg_color = (0, 0, 0, 0)

    def update_text(self, text: str):
        self.text = text
        self.size = self.label.texture_size
