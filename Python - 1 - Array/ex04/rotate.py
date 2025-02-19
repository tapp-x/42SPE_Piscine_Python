from PIL import Image
import numpy as np
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


def print_tab_row(tab):
    """
    Print a formatted display of the first and last elements
    For the first row of a given array,
    print the 3 first and 3 last elements separate with "..."
    Do the same for the last row.

    Parameters:
    tab (list): The array to display.
    """
    print(f"[[{tab[0][0]} {tab[0][1]} {tab[0][2]} ... \
{tab[0][-3]} {tab[0][-2]} {tab[0][-1]}]]")
    print(" ...")
    print(f"[[{tab[-1][0]} {tab[-1][1]} {tab[-1][2]} ... \
{tab[-1][-3]} {tab[-1][-2]} {tab[-1][-1]}]]")


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
        img2 = img.crop((450, 100, 850, 500))
        gray = img2.convert("L")
        print(f"The shape of the image is: ({gray.size[0]},\
{gray.size[1]}, {len(gray.getbands())}) or {gray.size}")
        print_tab(np.array(gray), gray.getbands())
        transp = gray.transpose(Image.FLIP_LEFT_RIGHT)
        tr = transp.transpose(Image.ROTATE_90)
        print(f"New shape after Transpose: ({tr.size[0]}, {tr.size[1]})")
        print_tab_row(np.array(tr))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
