from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
import time
from tkinter import Tk
from tkinter import messagebox


# fin = np.array()
path = "D:\PythonProjekty\DigitRecognition\Skrypty\data.jpg"


def clean_arr(ar):
    for q in range(28):
        for w in range(28):
            if ar[(q, w)] < 20:
                ar[(q, w)] = 0
    return ar


def jpg_image_to_array(ref):
  """
  Loads JPEG image into 3D Numpy array of shape
  (width, height, channels)
  """
  with Image.open(ref) as image:
      im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
      im_arr = im_arr.reshape((image.size[1], image.size[0], 3))
      return im_arr



def return_bit_arr():
    ar = jpg_image_to_array(path)
    ar=ar[:,:,0]
    ar=ar.astype(float)

    # br=ar-255
    # cr=np.abs(br)

    return ar
    # plt.imshow(ar, cmap=plt.cm.binary)
    # plt.show()


def print_result_of_prediction(a):
    Tk().wm_withdraw()  # to hide the main window
    ans = ""
    ans = messagebox.askquestion('Question', f'Did you draw {a} ?')

    """"
    if ans =='yes':
        messagebox.showinfo('PopUp', 'No to zajebiscie')
    if ans =='no':
        messagebox.showinfo('PopUp', 'Chujowo rysujesz')
    else:
        pass
    """
if __name__ == '__main__':
    temp = return_bit_arr()
    print(type(temp))