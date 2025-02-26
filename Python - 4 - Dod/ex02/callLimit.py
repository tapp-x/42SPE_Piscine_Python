def callLimit(limit: int):
    """
    Function that takes as argument a call
    limit of another function and blocks
    its execution above a limit.
    """
    count = 0

    def callLimiter(function):
        """
        Decorator function that takes as argument
        """
        def limit_function(*args: any, **kwds: any):
            """
            Function that limits the number of calls
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} called too many times")
        return limit_function
    return callLimiter
