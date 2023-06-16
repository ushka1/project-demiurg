from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivymd.uix.textfield import MDTextField

from ui_game.widgets.input_label import InputLabel
from ui_game.widgets.oldschool_button_game import OldschoolButtonGame

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
        self.dialog = None
        self.app = App.get_running_app()

        self.app.game_screen = self

    def reformat_with_player_name(self, text: str) -> str:
        return text.replace("{name}", self.ids.player_name.text)

    def _reset_input_backgrounds(self):
        for child in self.ids.stack.children:
            child.reset_background()

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
            self._show_restart_button()
            return

        message = self.app.runtime.get_message()
        if message:
            text += "\n\n" + "Message: " + message

        available_quest_stages = self.app.runtime.get_available_quest_stages()
        if available_quest_stages:
            text += "\n"
            for quest_stage in available_quest_stages:
                text += f"\nQuest: {quest_stage.quest.name}\n"
                text += quest_stage.text + "\n"

                # for option in quest_stage.options.values():
                #     text += f"Option {option.id}: " + option.text + "\n"

        # text += "\n\nAvailable exits:"

        self.description = self.reformat_with_player_name(text)

    def clear_input_stack(self):
        to_remove = self.ids.stack.children[:]
        for item in to_remove:
            self.ids.stack.remove_widget(item)

    def _update_input_labels(self):
        self.clear_input_stack()

        available_quest_stages = self.app.runtime.get_available_quest_stages()
        if available_quest_stages:
            for quest_stage in available_quest_stages:

                for option in quest_stage.options.values():
                    input_label = InputLabel()
                    key = f"{quest_stage.quest.id} {quest_stage.id} {option.id}"
                    input_label.text = f">{quest_stage.quest.name}: {option.text}"
                    input_label.direction = key
                    input_label.type = "quest"
                    self.ids[key] = input_label
                    self.ids.stack.add_widget(input_label)

        available_exits = self.app.runtime.get_available_exits()
        if available_exits:
            for key, value in available_exits.items():
                input_label = InputLabel()
                input_label.text = f">{key}: {value.text}"
                input_label.direction = key
                input_label.type = "exit"
                self.ids[key] = input_label
                self.ids.stack.add_widget(input_label)

        if len(self.ids.stack.children) > 0:
            self._mark_input(self.ids.stack.children[-1].direction)
        else:
            self._reset_input_backgrounds()

    def _show_restart_button(self):
        self.ids.restart_button.pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def on_kv_post(self, *args):
        self.rerender()
        self.set_name()

    def set_name(self):
        player_name = self.app.runtime.get_player_name()
        if player_name is None:
            Clock.schedule_once(lambda x: self.open_dialog())
        else:
            self.ids.player_name.text = player_name

    def open_dialog(self):
        self.dialog = MDDialog(
            title="Name your character:",
            type="custom",
            content_cls=MDTextField(),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_press=lambda x: self.confirm_name()
                ),
            ],
        )
        self.dialog.open()

    def confirm_name(self):
        name = self.dialog.content_cls.text
        self.app.runtime.set_player_name(name)
        self.ids.player_name.text = name
        self.dialog.dismiss()
        self.dialog = None

    def rerender(self):
        self._update_description()
        self._update_input_labels()

    def handle_keyboard(self, key):
        if len(self.ids.stack.children) == 0 or self.dialog:
            return

        stack = self.ids.stack
        scroll_stack = self.ids.scroll_stack

        if key == KEYS["enter"]:
            input_type = self.marked_input.type
            if input_type == "exit":
                self.app.runtime.select_exit(self.marked_input.direction)
            elif input_type == "quest":
                quest_id, stage_id, option_id = self.marked_input.direction.split(" ")
                self.app.runtime.select_quest_stage_option(quest_id, stage_id, option_id)

        elif key == KEYS["arrow-down"]:
            index = stack.children.index(self.marked_input) - 1
            if index < 0 or index >= len(stack.children):
                index = stack.children.index(self.marked_input)

            to_mark = stack.children[index].direction
            self._mark_input(to_mark)

            # if scroll_stack.scroll_y > 0:
            #     scroll_stack.scroll_y -= 0.15
            #     scroll_stack.scroll_y = min(scroll_stack.scroll_y, 0)

        elif key == KEYS["arrow-up"]:
            index = stack.children.index(self.marked_input) + 1
            if index < 0 or index >= len(stack.children):
                index = stack.children.index(self.marked_input)

            to_mark = stack.children[index].direction
            self._mark_input(to_mark)

            # if scroll_stack.scroll_y < 1:
            #     scroll_stack.scroll_y += 0.15
            #     scroll_stack.scroll_y = max(scroll_stack.scroll_y, 1)