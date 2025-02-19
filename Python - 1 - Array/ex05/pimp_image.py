import numpy as np
from PIL import Image
from load_image import ft_load


def ft_invert(array):
    """
    Invert the colors of an image.

    Parameters:
    array (list): The array to invert.
    """
    invert = 255 - array
    img = Image.fromarray(invert)
    img.show()


def ft_red(array):
    """
    Applying the red filter to an image.

    Parameters:
    array (list): The array to apply the filter to.
    """
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    img = Image.fromarray(array)
    img.show()


def ft_green(array):
    """
    Applying the green filter to an image.

    Parameters:
    array (list): The array to apply the filter to.
    """
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    img = Image.fromarray(array)
    img.show()


def ft_blue(array):
    """
    Applying the blue filter to an image.

    Parameters:
    array (list): The array to apply the filter to.
    """
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    img = Image.fromarray(array)
    img.show()


def ft_grey(array):
    """
    Applying the grayscale filter to an image.

    Parameters:
    array (list): The array to apply the filter to.
    """
    img = ft_load("landscape.jpg")
    img = img.astype(np.float32)
    gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
    img[:, :, 0] = gray
    img[:, :, 1] = gray
    img[:, :, 2] = gray
    grey = Image.fromarray(img.astype(np.uint8))
    # grey.save("landscape_grey.jpg") #To compare shapes, uncomment
    # ft_load("landscape_grey.jpg")
    grey.show()
