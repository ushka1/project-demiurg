from library.library import Library
from runtime.runtime import Runtime

library = Library()
library.load_game("mighty-roomba")

game_data = library.get_game_data()
game_state = library.get_game_state()

runtime = Runtime(game_data, game_state)
runtime.start()

print("\nThanks for playing!")
