import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

def crop_image(img, crop_range):
    '''
    The function crop input image.

    input:
    img- input image (array like numpy),
    crop_range- rectangular range (x1,y1)->(x2,y2), specified as a index number (list of coordinate),

    output:
    cropped_img- cropped image (array like numpy),

    '''
    x1=min(crop_range[0][0],crop_range[1][0])
    x2=max(crop_range[0][0],crop_range[1][0])
    y1=min(crop_range[0][1],crop_range[1][1])
    y2=max(crop_range[0][1],crop_range[1][1])
    cropped_img=img[y1:y2, x1:x2]

    return cropped_img

def display_image(img, window_name, window_size, delay):
    '''
    The function display image on specific window.

    input:
    img- input image (array like numpy),
    window_name- window name (string),
    window_size- window size (tuple),
    delay- delay for waiting[ms], 0 infinite waiting for key event (float)

    output:
    none
    '''
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, window_size)
    cv2.imshow(window_name, img)
    cv2.waitKey(delay)
    cv2.destroyWindow(window_name)

