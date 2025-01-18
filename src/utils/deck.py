import random
from utils.tiles import TILE_5, TILE_COUNT_DICT

class Deck:
    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):
        for tile, count in TILE_COUNT_DICT.items():
            for _ in range(count):
                self.deck.append(tile)

    def shuffle_deck(self):
        random.shuffle(self.deck)
        # Ensure the starting tile is a Tile object
        self.deck.insert(0, TILE_5)

    def draw_tile(self):
        return self.deck.pop(0)

    def get_deck(self):
        return self.deck

    def get_deck_size(self):
        return len(self.deck)

    def reset_deck(self):
        self.deck = []
        self.create_deck()
        self.shuffle_deck()