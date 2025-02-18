from load_image import ft_load
from PIL import Image
import numpy as np
import cv2
import os

def print_tab(tab, channels):
    """
    Print a formatted display of the first and last elements
    in each row of a given array.

    Parameters:
    tab (list): The array to display.
    channels (int): The number of channels in the image.
    """
    tab_len = len(tab)
    count = 0
    for row in tab:
        if count == 0:
            if channels != 3:
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > tab_len - 4:
            if channels != 3:
                if count == tab_len - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < tab_len - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == tab_len - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1


def main():
    """
    A program that should load the image "animal.jpeg", print some information
    about it and display it after "zooming" in on a specific area.

    Error handling is included to catch any exceptions that may occur.
    """
    try:
        path = "animal.jpeg"
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        ft_load("animal.jpeg")
        print("Original shape: ", img.size)
        print_tab(np.array(img), len(img.getbands()))
        img2 = img.crop((400, 100, 800, 500))
        img2.save("zoomed.jpeg")
        gray = img2.convert("L")
        print(f"New shape after slicing: ({gray.size[0]}, {gray.size[1]}, {len(gray.getbands())}) or {gray.size}")
        print_tab(np.array(gray), gray.getbands())
        gray.show()


    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()