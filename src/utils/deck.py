import random
from utils.tiles import TILE_COUNT_DICT

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
        self.deck.insert(0, 'tile_5') # the starting tile.

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

class Tile:
    def __init__(self, tile_type, file_name):
        self.tile_type = tile_type
        self.file_name = file_name

    def get_tile_type(self):
        return self.tile_type
    
    def get_file_name(self):
        return self.file_name
    