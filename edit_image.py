from PIL import Image
from io import BytesIO
import cv2
import numpy as np

def add_images(img1,img2):
    img1,img2=tuple(map(lambda img:np.array(img),[img1,img2]))
    img_output = Image.fromarray(cv2.add(img1, img2))
    return img_output