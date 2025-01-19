from enum import Enum

from utils.deck import Deck
class GameState(Enum):
    MAIN_MENU = 0
    PLAY = 1
    QUIT = 2

class GameStateContext:
    def __init__(self):
        self.deck = Deck()
        self.placed_tiles = []
