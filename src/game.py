import raylibpy as rl

from utils.enums import GameState

def play_game(gs):
    """
    Placeholder for the actual game logic.
    """
    screen_width = rl.get_screen_width()
    screen_height = rl.get_screen_height()

    rl.draw_text("Game is starting!", screen_width // 2 - 100, screen_height // 2, 30, rl.DARKGRAY)

    # Go back to the menu when ESC is pressed
    if rl.is_key_pressed(rl.KEY_ESCAPE):
        return GameState.MAIN_MENU

    return gs