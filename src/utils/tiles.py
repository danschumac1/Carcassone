
from enum import Enum
from typing import Dict, Optional

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
        self.edges = edges  # Dictionary mapping Dir -> Edge
        self.features = features  # Dictionary mapping TileFeatures -> bool
        self.file_name = file_name  # Associated image file for the tile

    def rotate(self, direction: str = "right"):
        """
        Rotates the tile clockwise (right) or counterclockwise (left).

        Parameters:
            direction (str): 'right' for clockwise, 'left' for counterclockwise.

        Returns:
            None
        """
        if direction not in {"right", "left"}:
            raise ValueError("Invalid direction. Use 'right' or 'left'.")

        # Rotation logic: Shift directions
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

    def __repr__(self):
        return f"Tile(edges={self.edges}, features={self.features}, file_name='{self.file_name}')"

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
    TILE_15: 5, # 2 sheilds, 3 regular
    TILE_16: 4, # 1 sheilds, 3 regular
    TILE_17: 3, # 1 sheilds, 2 regular
    TILE_18: 3, # 2 sheilds, 1 regular
    TILE_19: 1, # 1 sheilds, 0 regular
}