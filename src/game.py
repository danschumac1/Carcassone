import raylibpy as rl

from utils.enums import GameState
from utils.deck import Deck

def play_game(gs):
    screen_width = rl.get_screen_width()
    screen_height = rl.get_screen_height()

    deck = Deck()
    deck.create_deck()
    deck.shuffle_deck()
    starting_tile = deck.draw_tile()
    starting_tile.place_tile(screen_width//2, screen_height//2)  # This will now work

    # rl.draw_text("Game is starting!", screen_width // 2 - 100, screen_height // 2, 30, rl.DARKGRAY)

    if rl.is_key_pressed(rl.KEY_ESCAPE):
        return GameState.MAIN_MENU

    return gs