def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for each pair of height and weight.
    Args:
        height (list[int | float]): Heights in meters.
        weight (list[int | float]): Weights in kg.
    Returns:
        list[int | float]: Calculated BMI values.
    Raises:
        ValueError: If lengths of height and weight lists do not match.
        TypeError: If any element in lists is not int or float.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of same length.")
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height list elements must be int or float.")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight list elements must be int or float.")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values exceed the limit.
    Args:
        bmi (list[int | float]): BMI values.
        limit (int): Limit to compare against.
    Returns:
        list[bool]: True if BMI exceeds limit, else False.
    Raises:
        TypeError: If element in list or limit is not int or float.
    """
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI list elements must be int or float.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an int.")
    return [b > limit for b in bmi]
