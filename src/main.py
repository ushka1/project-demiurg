from config.globals import ui_type
from library.library import Library

if ui_type == "kivy":
    library = Library()


if ui_type == "console":
    from runtime.runtime import Runtime

    library = Library()
    game_data, game_progress = library.load_game("Mighty Roomba")

    runtime = Runtime(game_data, game_progress, library)

    print("\nThanks for playing!")
