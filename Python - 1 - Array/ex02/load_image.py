from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    filename = "./img.png"
    img = Image.open(filename, 'r')
    # pix = list(img.getdata())
    array = np.array(img.getdata())
    print(f"The shape of the image is: {array.shape}")
    print(array[0,0])
    return (array)