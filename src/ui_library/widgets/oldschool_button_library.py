from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


Builder.load_file('ui_library/widgets/oldschool_button_library.kv')


class OldschoolButtonLibrary(MDCard):
    text = StringProperty()

