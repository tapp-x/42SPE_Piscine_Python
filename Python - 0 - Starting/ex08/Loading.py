import sys
import time


def ft_tqdm(lst: range) -> None:
    """
    A homemade version of tqdm : simulate a progress bar
    with the yield operator

    Args:
        - range to iterate

    For the yield part:
    The yield operator in Python is used to create a generator,
    which is a type of iterable. When a function contains a yield
    statement, it becomes a generator function. Instead of returning
    a single value and terminating, a generator function can yield
    multiple values, one at a time, and maintain its state between each yield.
    """
    total = len(lst)
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100
        b = '=' * int(percent // 2) + '>' + '-' * (50 - int(percent // 2) - 1)
        sys.stdout.write(f'\r{percent:.2f}%|[{b}]| {i + 1}/{total}')
        sys.stdout.flush()
        yield item
        time.sleep(0.01)
    sys.stdout.write('\n')
