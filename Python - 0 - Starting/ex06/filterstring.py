import sys
from ft_filter import ft_filter


def main():
    """
    This program takes 2 args : a string(S) and an int(N)
    It output a list of words from S that have a length greater than N
    If the number of argument is different from 2,
    or if the type of any argument is wrong,
    the program prints an AssertionError.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        s = str(sys.argv[1])
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = s.split()
    filtered_words = list(ft_filter(lambda word: len(word) > n, words))
    print(filtered_words)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
