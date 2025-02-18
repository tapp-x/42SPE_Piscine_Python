from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the file path and converts it to a NumPy array.

    Parameters:
    path (str): The file path to the image.

    Returns:
    list: A NumPy array representing the image.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        array = np.array(img)
        print(f"The shape of the image is: {array.shape}")
        return array
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return ""
