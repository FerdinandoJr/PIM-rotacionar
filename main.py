import numpy as np
import matplotlib.pyplot as plt
import imutils 
import cv2  
from matplotlib import pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

path = '/content/drive/MyDrive/PIM/'
image = cv2.imread(path+"verticalBars.png")  


def rotacionar(image, ang=0):
  Rotated_image = imutils.rotate(image, angle=ang) 
  #cv2.imshow(Rotated_image) 
  plt.imshow(Rotated_image)
  plt.show()
  

ang = 0
rotacionar(image, 0)
for i in range(6):
  ang += 15
  rotacionar(image, -ang)
