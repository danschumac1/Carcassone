"""
Created on 01/18/2025

@author: Dan
TO RUN:
python ./src/main.py
"""

from enum import Enum
import raylibpy as rl
from utils.constants import WIDTH, HEIGHT
from game import play_game
from utils.enums import GameState



def initialize_window():
    rl.init_window(WIDTH, HEIGHT, "HoneyPy")
    rl.set_target_fps(60)


def main_menu(gs):
    """
    Handles the main menu logic.
    Draws the menu and allows the user to select "Play" or "Quit."
    """
    screen_width = rl.get_screen_width()
    screen_height = rl.get_screen_height()

    # Button dimensions
    button_width = 200
    button_height = 50

    # Button positions
    play_button_x = (screen_width - button_width) // 2
    play_button_y = screen_height // 2 - 60

    quit_button_x = (screen_width - button_width) // 2
    quit_button_y = screen_height // 2 + 10

    # Colors
    button_color = rl.LIGHTGRAY
    hover_color = rl.GRAY
    text_color = rl.DARKGRAY

    # Draw the menu
    rl.draw_text("CARCASSONNE", screen_width // 2 - 200, 100, 50, rl.DARKGREEN)
    
    # Play button
    if rl.check_collision_point_rec(rl.get_mouse_position(), 
                                    rl.Rectangle(play_button_x, play_button_y, button_width, button_height)):
        rl.draw_rectangle(play_button_x, play_button_y, button_width, button_height, hover_color)
        if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            return GameState.PLAY  # Switch to play state
    else:
        rl.draw_rectangle(play_button_x, play_button_y, button_width, button_height, button_color)
    rl.draw_text("PLAY", play_button_x + 50, play_button_y + 10, 30, text_color)

    # Quit button
    if rl.check_collision_point_rec(rl.get_mouse_position(), 
                                    rl.Rectangle(quit_button_x, quit_button_y, button_width, button_height)):
        rl.draw_rectangle(quit_button_x, quit_button_y, button_width, button_height, hover_color)
        if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            return GameState.QUIT  # Exit the game
    else:
        rl.draw_rectangle(quit_button_x, quit_button_y, button_width, button_height, button_color)
    rl.draw_text("QUIT", quit_button_x + 50, quit_button_y + 10, 30, text_color)

    return gs  # Stay in main menu

def main():
    """
    The main function initializes the game window and runs the game loop.
    """
    initialize_window()

    state_handler = {
        GameState.MAIN_MENU: main_menu,
        GameState.PLAY: play_game,
    }

    gs = GameState.MAIN_MENU

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)  # Always clear at the start of each frame

        if gs in state_handler:
            gs = state_handler[gs](gs)
        else:
            print("Invalid game state")
            break

        rl.end_drawing()

    rl.close_window()


if __name__ == "__main__":
    main()
