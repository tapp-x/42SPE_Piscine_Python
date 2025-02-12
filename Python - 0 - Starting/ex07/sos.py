import sys


def morse_encoder(string):
    """
    Take a string in paramater and encode it into morse code
    Only support alphanumeric and space
    """
    morse_dictionary = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": "/",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    input_string = string.upper()
    morse_code = []

    for char in input_string:
        if char in morse_dictionary:
            morse_code.append(morse_dictionary[char])
        else:
            print("AssertionError: the arguments are bad")
            return
    print(" ".join(morse_code))


def main():
    if len(sys.argv) != 2:
        print("Usage: python sos.py <string>")
        return
    morse_encoder(sys.argv[1])


if __name__ == "__main__":
    main()
