from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.app import App


from ui_game.widgets.input_label import InputLabel

Builder.load_file('ui_game/screens/game_screen.kv')


KEYS = {
    "enter": 13,
    "arrow-up": 273,
    "arrow-right": 275,
    "arrow-down": 274,
    "arrow-left": 276,
}


class GameScreen(MDScreen):
    description = StringProperty()
    available_exits: list
    marked_input: InputLabel

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

        self.app.game_screen = self

    def _reset_input_backgrounds(self):
        for key in "NESW":
            self.ids[key].reset_background()

    def _mark_input(self, direction: str):
        self._reset_input_backgrounds()
        self.ids[direction].set_active_background()
        self.marked_input = self.ids[direction]

    def _update_description(self):
        current_location = self.app.runtime.get_current_location()
        text = "Location: " + current_location.name
        text += "\n" + current_location.text

        if current_location.is_end_location:
            self.description = text
            return

        text += "\n\nAvailable exits:"

        message = self.app.runtime.get_message()
        if message:
            text += "\n\n" + "Message: " + message

        self.description = text

    def _update_input_labels(self):
        self.available_exits = []

        available_exits = self.app.runtime.get_available_exits()
        i = 0
        if available_exits:
            for key, value in available_exits.items():
                self.ids[key].text = key + ": " + value.text
                self.ids[key].index = i
                i += 1
                self.available_exits.append(key)

        for key in "NESW":
            if key not in available_exits:
                self.ids[key].text = ""

        if len(self.available_exits) > 0:
            self._mark_input(self.available_exits[0])
        else:
            self._reset_input_backgrounds()

    def on_enter(self, *args):
        Clock.schedule_once(lambda x: self.rerender())

    def rerender(self):
        self._update_description()
        self._update_input_labels()

    def handle_keyboard(self, key):
        if key == KEYS["enter"]:
            self.app.runtime.select_exit(self.marked_input.direction)

        elif key == KEYS["arrow-down"]:
            index = self.marked_input.index + 1
            if index < 0 or index >= len(self.available_exits):
                index = self.marked_input.index

            to_mark = self.available_exits[index]
            self._mark_input(to_mark)

        # elif key == KEYS["arrow-right"]:
        #     self._mark_input("E")

        elif key == KEYS["arrow-up"]:
            index = self.marked_input.index - 1
            if index < 0 or index >= len(self.available_exits):
                index = self.marked_input.index

            to_mark = self.available_exits[index]
            self._mark_input(to_mark)

        # elif key == KEYS["arrow-left"]:
        #     self._mark_input("W")
