from player import Player
from ui import UI

player = Player()
player.set_name("Demiurg")

ui = UI()
ui.print(f"Hello {player.name}!")
