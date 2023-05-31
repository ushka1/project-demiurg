from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


Builder.load_file('ui_library/widgets/main_screen_button.kv')


class MainScreenButton(MDCard):
    text = StringProperty()
    purpose = StringProperty()

    # def on_touch_down(self, touch):
    #     touch_x, touch_y = touch.pos
    #     image_x = self.ids.image.pos[0]
    #     image_y = self.ids.image.top
    #     width, height = self.ids.image.texture_size
    #     if image_x <= touch_x <= image_x + width and image_y <= touch_y <= image_y + height:
    #         App.get_running_app().root.ids.screen_manager.current = self.purpose
