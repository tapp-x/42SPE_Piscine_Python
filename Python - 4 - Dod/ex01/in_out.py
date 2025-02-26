def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return the exponantiation of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Function that return an object that when called
    return the result of the calculation of x and the function.
    """
    count = 0

    def inner():
        nonlocal count
        count += 1
        for i in range(count):
            if i == 0:
                result = function(x)
            else:
                result = function(result)
        return result
    return inner
