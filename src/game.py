import raylibpy as rl

from utils.constants import HEIGHT, WIDTH
from utils.enums import GameState
from utils.deck import Deck
from utils.tiles import Tile, draw_all_placed_tiles

def play_game(gs):
    print("INITIALIZING DECK")
    deck = Deck()
    deck.reset_deck()
    placed_tiles = []

    print("Picking up STARTING TILE")
    starting_tile = deck.draw_tile()

    center_width = (WIDTH - starting_tile.width) // 2
    center_height = (HEIGHT - starting_tile.height) // 2
    print("PLACING STARTING TILE")
    starting_tile.place_tile(center_width, center_height, placed_tiles)

    tile = deck.draw_tile()
    while gs == GameState.PLAY:
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        draw_all_placed_tiles(placed_tiles)

        if tile.placed and not deck.is_empty:
            tile = deck.draw_tile()

        if not tile.placed:
            tile.follow_mouse()

        if rl.is_mouse_button_pressed(rl.MOUSE_RIGHT_BUTTON):
            print("Right mouse button pressed.")
            tile.rotate("right")

        if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            tile.place_tile(rl.get_mouse_x(), rl.get_mouse_y(), placed_tiles)

        # State transition logic
        if rl.is_key_pressed(rl.KEY_ESCAPE):
            print("ESC pressed. Returning to main menu.")
            gs = GameState.MAIN_MENU
        
        if tile.placed and deck.is_empty:
            print("Deck is empty. And placed last tile. Exiting game.")
            gs = GameState.MAIN_MENU

        rl.end_drawing()

    return gs
