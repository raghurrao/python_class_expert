"""
Week 1 Challenge: NumPy Image Processing

In this challenge, you will implement core image processing algorithms using only NumPy.
An RGB image is represented as a 3D NumPy array of shape (Height, Width, 3), where elements
are unsigned 8-bit integers (uint8) ranging from 0 to 255.

Do not use loops (for/while) in your implementations; all operations must be vectorized!
"""

import numpy as np

def convert_to_grayscale(rgb_image: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image of shape (H, W, 3) to a Grayscale image of shape (H, W).
    Formula:
    Y = 0.2989 * R + 0.5870 * G + 0.1140 * B
    
    Make sure to:
    1. Extract R, G, B channels using slicing.
    2. Multiply each channel by its weight and sum them together.
    3. Cast the final result to uint8 using `.astype(np.uint8)`.
    """
    # TODO: Implement your solution here
    pass


def crop_image(image: np.ndarray, row_start: int, row_end: int, col_start: int, col_end: int) -> np.ndarray:
    """
    Crop the image (can be RGB (H, W, 3) or Grayscale (H, W)) to keep only the rows from
    row_start to row_end (exclusive) and columns from col_start to col_end (exclusive).
    
    Use NumPy slicing.
    """
    # TODO: Implement your solution here
    pass


def adjust_brightness(image: np.ndarray, factor: float) -> np.ndarray:
    """
    Adjust the brightness of the image (RGB or Grayscale) by multiplying all pixels by `factor`.
    
    Make sure to:
    1. Multiply the array values by `factor` (floating point math).
    2. Clip the values to remain within the [0.0, 255.0] range using `np.clip` so that 
       no values overflow or underflow.
    3. Cast the result back to `np.uint8` before returning.
    """
    # TODO: Implement your solution here
    pass


def invert_colors(rgb_image: np.ndarray) -> np.ndarray:
    """
    Invert the colors of an RGB image.
    Formula: inverted_channel = 255 - original_channel
    
    Make sure to return the result as uint8.
    """
    # TODO: Implement your solution here
    pass
