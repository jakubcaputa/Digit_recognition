import Image
import numpy as np

im = Image.load('nr33.jpg')
im = im.convert('L')

arr = np.fromiter(iter(im.getdata()), np.uint8)
arr.resize(im.height, im.width)

arr ^= 0xFF  # invert
inverted_im = Image.fromarray(arr, mode='L')
inverted_im.show()