
from enum import Enum
from typing import Dict, Optional
import raylibpy as rl 

# Enums for clarity
class Edge(Enum):
    ROAD = 1
    CITY = 2
    FIELD = 3

class TileFeatures(Enum):
    ROAD = 1
    CITY = 2
    MONASTERY = 3

class Dir(Enum):
    N = 1
    E = 2
    S = 3
    W = 4

class Tile:
    def __init__(self, edges: Dict[Dir, Optional[Edge]], features: Dict[TileFeatures, bool], file_name: Optional[str] = None):
        if set(edges.keys()) != {Dir.N, Dir.E, Dir.S, Dir.W}:
            raise ValueError("Edges dictionary must have all four directions: N, E, S, W.")
        
        self.edges = edges
        self.features = features
        self.file_name = file_name
        self.texture = None  # Cached texture

    def __repr__(self):
        return f"Tile(edges={self.edges}, features={self.features}, file_name='{self.file_name}')"

    def rotate(self, direction: str = "right"):
        if direction not in {"right", "left"}:
            raise ValueError("Invalid direction. Use 'right' or 'left'.")

        if direction == "right":
            self.edges = {
                Dir.N: self.edges[Dir.W],
                Dir.E: self.edges[Dir.N],
                Dir.S: self.edges[Dir.E],
                Dir.W: self.edges[Dir.S],
            }
        elif direction == "left":
            self.edges = {
                Dir.N: self.edges[Dir.E],
                Dir.E: self.edges[Dir.S],
                Dir.S: self.edges[Dir.W],
                Dir.W: self.edges[Dir.N],
            }

    def load_image(self):
        if self.file_name is None:
            raise ValueError("No image file associated with this tile.")

        try:
            pre_path = "./images/tiles"  # Path to the tiles folder
            print(f"Loading image: {pre_path}/{self.file_name}")  # Debug print
            image = rl.load_image(f"{pre_path}/{self.file_name}")
            self.texture = rl.load_texture_from_image(image)
            rl.unload_image(image)
            return self.texture
        except Exception as e:
            raise RuntimeError(f"Failed to load image '{self.file_name}': {e}")

    def _draw(self, x: int, y: int):
        if self.texture is None:
            print("Texture not loaded, loading now...")  # Debug print
            self.load_image()
            
        rl.draw_texture(self.texture, x, y, rl.WHITE)

    def unload_texture(self):
        if self.texture:
            rl.unload_texture(self.texture)
            self.texture = None

    def follow_mouse(self):
        x, y = map(int, rl.get_mouse_position())
        self._draw(x, y)

    def place_tile(self, x: int, y: int):
        self._draw(x, y)

############################################
TILE_1 = Tile(
    edges={
        Dir.N: Edge.ROAD,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.FIELD,
    },
    features={
        TileFeatures.ROAD: True,
    },
    file_name="tile_1.png"
)

TILE_2 = Tile(
    edges={
        Dir.N: Edge.ROAD,
        Dir.E: Edge.ROAD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.ROAD,
    },
    features={
        TileFeatures.ROAD: True,
    },
    file_name="tile_2.png"
)

TILE_3 = Tile(
    edges={
        Dir.N: Edge.FIELD,
        Dir.E: Edge.ROAD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.ROAD,
    },
    features={
        TileFeatures.ROAD: True,
    },
    file_name="tile_3.png"
)

TILE_4 = Tile(
    edges={
        Dir.N: Edge.FIELD,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.ROAD,
    },
    features={
        TileFeatures.ROAD: True,
    },
    file_name="tile_4.png"
)  

TILE_5 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.ROAD,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.ROAD,
    },
    features={
        TileFeatures.ROAD: False,
        TileFeatures.CITY: True,
    },
    file_name="tile_5.png"
)

TILE_6 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.ROAD,
    },
    features={
        TileFeatures.ROAD: False,
        TileFeatures.CITY: True,
    },
    file_name="tile_6.png"
)

TILE_7 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.ROAD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.FIELD,
    },
    features={
        TileFeatures.ROAD: False,
        TileFeatures.CITY: True,
    },
    file_name="tile_7.png"
)

TILE_8 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.ROAD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.ROAD,
    },
    features={
        TileFeatures.ROAD: True,
        TileFeatures.CITY: True,
    },
    file_name="tile_8.png"
)

TILE_9 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.FIELD,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_9.png"
)

TILE_10 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_10.png"
)

TILE_11 = Tile(
    edges={
        Dir.N: Edge.FIELD,
        Dir.E: Edge.CITY,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True, # TODO THESE ARE 2 different cities! ???
    },
    file_name="tile_11.png"
)

TILE_12 = Tile(
    edges={
        Dir.N: Edge.FIELD,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.FIELD,
    },
    features={
        TileFeatures.MONASTERY: True,
    },
    file_name="tile_12.png"
)

TILE_13 = Tile(
    edges={
        Dir.N: Edge.FIELD,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.FIELD,
    },
    features={
        TileFeatures.MONASTERY: True,
        TileFeatures.ROAD: True,
    },
    file_name="tile_13.png"
)

TILE_14 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.ROAD,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
        TileFeatures.ROAD: True,
    },
    file_name="tile_14.png"
)

TILE_15 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.FIELD,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_15.png"
)

TILE_16 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.CITY,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_16.png"
)

TILE_17 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.CITY,
        Dir.S: Edge.ROAD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_17.png"
)

TILE_18 = Tile(
    edges={
        Dir.N: Edge.FIELD,
        Dir.E: Edge.CITY,
        Dir.S: Edge.FIELD,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_18.png"
)

TILE_19 = Tile(
    edges={
        Dir.N: Edge.CITY,
        Dir.E: Edge.CITY,
        Dir.S: Edge.CITY,
        Dir.W: Edge.CITY,
    },
    features={
        TileFeatures.CITY: True,
    },
    file_name="tile_19.png"
)

# TODO: change to tuples or dictionary for sheilds and regular tiles 
            # (LATER, KEEP IT SIMPLE FOR NOW)
TILE_COUNT_DICT = {
    TILE_1: 8,
    TILE_2: 1,
    TILE_3: 4,
    TILE_4: 9,
    TILE_6: 3,
    TILE_7: 3,
    TILE_15: 5,
    TILE_16: 4,
    TILE_17: 3,
    TILE_18: 3,
    TILE_19: 1,
    TILE_5: 1  # Include TILE_5 in the dictionary
}