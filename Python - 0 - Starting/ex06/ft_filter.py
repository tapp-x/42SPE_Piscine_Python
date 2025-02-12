def ft_filter(function, iterable):
    """
    iterable: a list of object
    function: a function that return true or false

    Return an iterator yielding those items of
    iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function(item))
