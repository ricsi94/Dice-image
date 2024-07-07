# Improting Image class from PIL module
from PIL import Image


def cropimage(image,dice):
    # Opens an image in RGB mode
    im = Image.open(image)
    width, height = im.size

    #Remains
    x = width % dice
    y = height % dice

    left = 0
    top = 0
    right = width - x
    bottom = height - y

    im1 = im.crop((left, top, right, bottom))

    width, height = im1.size

    CroppedImage = [im1,width,height]
    return CroppedImage




