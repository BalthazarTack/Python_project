import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

image=PIL.Image.open("screenshot.jpg")
pixel=image.load()

def hex_iteration(img,hex_size):
    pix=img.load()
    img=np.array(img)
    w,h,_=img.shape

    return(w,h)

