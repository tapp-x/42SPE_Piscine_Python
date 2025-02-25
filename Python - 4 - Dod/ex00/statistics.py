def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Take a quantity of unknown number and
    compute the mean, median, quartile, std
    and var according to the kwargs ask

    Parameters:
        args (any): All numbers to compute
        kwargs (any): The type of statistics to compute
    """

    if not all(isinstance(arg, (int, float)) for arg in args):
        return

    valid_stats = ["mean", "median", "quartile", "std", "var"]

    for key, value in kwargs.items():
        if value not in valid_stats:
            continue

        if value == "mean":
            if (len(args) == 0):
                print("ERROR")
                continue
            print(f"mean: {sum(args) / len(args)}")
        elif value == "median":
            if (len(args) == 0):
                print("ERROR")
                continue
            sort = sorted(args)
            mid = len(sort) // 2
            if len(sort) % 2 == 0:
                print(f"median: {(sort[mid - 1] + sort[mid]) / 2}")
            else:
                print(f"median: {sort[mid]}")
        elif value == "quartile":
            if (len(args) == 0):
                print("ERROR")
                continue
            sorted_args = sorted(args)
            quart = len(sorted_args) // 4
            Q1 = sorted_args[quart]
            Q3 = sorted_args[(len(sorted_args) * 3) // 4]
            print(f"quartiles: [{float(Q1)}, {float(Q3)}]")
        elif value == "std":
            if (len(args) == 0):
                print("ERROR")
                continue
            mean = sum(args) / len(args)
            variance = sum((arg - mean) ** 2 for arg in args) / len(args)
            print(f"std: {variance ** 0.5}")
        elif value == "var":
            if (len(args) == 0):
                print("ERROR")
                continue
            mean = sum(args) / len(args)
            variance = sum((arg - mean) ** 2 for arg in args) / len(args)
            print(f"var: {variance}")
