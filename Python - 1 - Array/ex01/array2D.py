import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version
    based on the provided start and end arguments.

    Parameters:
    family (list): A 2D array (list of lists) to be sliced.
    start (int): The starting index for the slice.
    end (int): The ending index for the slice.

    Returns:
    list: A truncated version of the input 2D array.

    Error Handling:
    - If the input is not a list or the sublists are not of the same size,
      prints "AssertionError: {error}".
    """
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end must be integers")

        array = np.array(family)
        if len(array.shape) != 2:
            raise ValueError("Input is not a 2D array")
        print(f"My shape is: {array.shape}")
        if start < 0:
            start = array.shape[0] + start
        if end < 0:
            end = array.shape[0] + end
        array = array[start:end]
        print(f"My new shape is: {array.shape}")
        return array.tolist()
    except Exception as error:
        print(f"AssertionError: {error}")
