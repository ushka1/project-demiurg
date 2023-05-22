from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

Builder.load_file('ui/widgets/input_label.kv')


class InputLabel(MDCard):
    text = StringProperty()
    direction: str
    index: int

    def set_active_background(self):
        self.md_bg_color = (0, 1, 1, 1)

    def reset_background(self):
        self.md_bg_color = (0, 0, 0, 0)
