def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for each pair of height and weight.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of calculated BMI values.

    Raises:
        ValueError: If the lengths of the height and weight lists do not match.
        TypeError: If any element in the height or weight lists is not an int or float.
    """
    if len(height) != len(weight):
        raise ValueError("The lengths of the height and weight lists do not match.")
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("All elements in the height list must be int or float.")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("All elements in the weight list must be int or float.")
    bmi_list = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmi_list.append(bmi)
    return bmi_list

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to the BMI values to determine if they exceed the specified limit.

    Args:
    try:
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise TypeError("All elements in the bmi list must be int or float.")
        if not isinstance(limit, int):
            raise TypeError("The limit must be an int.")
        return [b > limit for b in bmi]
    except Exception as e:
        print(f"AssertionError: {e}")
        return []

    Raises:
        TypeError: If any element in the bmi list is not an int or float, or if limit is not an int.
    """
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("All elements in the bmi list must be int or float.")
    if not isinstance(limit, int):
        raise TypeError("The limit must be an int.")
    return [b > limit for b in bmi]


