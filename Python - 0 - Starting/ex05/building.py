import sys


def string_counter(string):
    """Arg string: the string to analyze

        Print this with de string input :
        - Size of the string
        - Number of uppercase
        - Number of lowercase
        - Number of punctuation marks
        - Number of space
        - Number of digit
        If empty input, enter a string """

    stringlen = len(string)
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    punct = sum(1 for c in string if c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    space_count = sum(1 for c in string if c.isspace())
    digit_count = sum(1 for c in string if c.isdigit())

    print(f"The text contains {stringlen} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
    """ - Handle input error and size of string
        - Throw AssertionError if too many args
        - Pass if EOF case"""
    input_string = ""
    try:
        if len(sys.argv) == 1:
            try:
                input_string = input("What's the string to enter?\n")
                input_string += "\n"
            except EOFError:
                pass
        else:
            assert len(sys.argv) <= 2, \
                "AssertionError: Too many arguments provided"
    except AssertionError as e:
        print(e)
        return
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
    string_counter(input_string)


if __name__ == "__main__":
    main()
