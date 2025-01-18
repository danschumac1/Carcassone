"""
Created on 01/17/2025

@author: Dan Schumacher

How to use:
python ./src/utils/images.py
"""

import os
import raylibpy as rl 
import sys
sys.path.append("./src")
from PIL import Image

def remove_custom_border(image_path, top, bottom, left, right, output_path):
    """
    Remove a white border of given sizes from the top, bottom, left, and right sides of the image.
    
    Parameters:
        image_path (str): Path to the input image.
        top (int): Number of pixels to remove from the top.
        bottom (int): Number of pixels to remove from the bottom.
        left (int): Number of pixels to remove from the left.
        right (int): Number of pixels to remove from the right.
        output_path (str): Path to save the output image.
    
    Returns:
        None
    """
    # Load the image
    image = Image.open(image_path)
    
    # Calculate new dimensions
    width, height = image.size
    new_left = left
    new_top = top
    new_right = width - right
    new_bottom = height - bottom
    
    # Crop the image
    cropped_image = image.crop((new_left, new_top, new_right, new_bottom))
    
    # Save the cropped image
    cropped_image.save(output_path)

# Define custom border removal parameters

def tile_splitter(num_rows: int, num_cols: int, image_path: str, output_folder: str = "./images/tiles"):
    '''
    Splits a tileset image into individual tiles and saves them to a folder.
    Assumes square tiles.

    Parameters:
        num_rows (int): Number of rows in the tileset image.
        num_cols (int): Number of columns in the tileset image.
        image_path (str): Path to the tileset image.
        output_folder (str): Path to the folder where the tiles will be saved.
    '''
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Load the image
    tileset = rl.load_image(image_path)

    # Tile information
    tile_width = tileset.width // num_cols
    tile_height = tileset.height // num_rows

    # Splice and save tiles
    tile_count = 0
    for y in range(num_rows):
        for x in range(num_cols):
            # Define the rectangle for the current tile
            tile_rec = rl.Rectangle(
                x * tile_width,
                y * tile_height,
                min(tile_width, tileset.width - x * tile_width),
                min(tile_height, tileset.height - y * tile_height)
            )
            # Extract the tile image
            tile_image = rl.image_from_image(tileset, tile_rec)
            # Create the filename
            filename = os.path.join(output_folder, f"tile_{tile_count}.png")
            # Export the tile to a file
            rl.export_image(tile_image, filename)
            # Unload the tile image
            rl.unload_image(tile_image)
            # Increment the tile counter
            tile_count += 1

    # Unload the original tileset
    rl.unload_image(tileset)
    print("Tile splicing and saving complete!")

if __name__ == "__main__":
    ##########################################
    # FIRST STEP
    ##########################################
    # image_fi = "./images/tiles/all_tiles.png"
    # image_fo = "./images/tiles/all_tiles_cleaned.png"
    # top = 9    # Adjust as needed
    # bottom = 12  # Adjust as needed
    # left = 11   # Adjust as needed
    # right = 16  # Adjust as needed
    # # tile_splitter(5, 4, image_path)
    # remove_custom_border(image_fi, top, bottom, left, right, image_fo)

    ##########################################
    # SECOND STEP
    ##########################################
    tile_splitter(4, 5, "./images/tiles/all_tiles_cleaned.png")