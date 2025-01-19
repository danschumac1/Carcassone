import random
from utils.tiles import TILE_5, TILE_COUNT_DICT

class Deck:
    def __init__(self):
        self.deck = []

    def create_deck(self):
        self.deck = []
        self.is_empty = False
        for tile, count in TILE_COUNT_DICT.items():
            for _ in range(count):
                tile.load_image()
                self.deck.append(tile)

    def shuffle_deck(self):
        random.shuffle(self.deck)
        # Ensure the starting tile is a Tile object
        self.deck.insert(0, TILE_5)

    def draw_tile(self):
        """Removes and returns the top tile from the deck."""
        if self.get_deck_size() <= 1:
            self.is_empty = True
        return self.deck.pop(0)

    def get_deck(self):
        return self.deck

    def get_deck_size(self):
        return len(self.deck)
    
    def reset_deck(self):
        self.create_deck()
        self.shuffle_deck()
        self.is_empty = False