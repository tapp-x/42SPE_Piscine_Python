import sys

if len(sys.argv) == 1:
    sys.exit(0)

try:
    assert len(sys.argv) == 2, "exactly one argument is required"
    numb = int(sys.argv[1])
except AssertionError as e:
    print(f"AssertionError: {e}")
    sys.exit(1)
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

if numb % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
