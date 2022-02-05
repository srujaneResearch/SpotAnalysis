import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

images_dir_path = 'images/Good'
filenames=os.listdir(images_dir_path)

IMG_SIZE = 640, 360
MARGIN_WIDTH = [round(IMG_SIZE[1]/4.5), round(IMG_SIZE[1]/4)]
MARGIN_HEIGHT = [round(IMG_SIZE[0]/5), round(IMG_SIZE[0]/5)]

for filename in filenames:
    img_path=os.path.join(images_dir_path, filename)
    gray_img=cv2.imread(img_path,0)
    img = cv2.resize(gray_img, IMG_SIZE)
    img = img[MARGIN_HEIGHT[0]:-MARGIN_HEIGHT[1],MARGIN_WIDTH[0]:-MARGIN_WIDTH[1]]
    
    cv2.namedWindow("Input", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Input', 640, 640)
    cv2.imshow('Input', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

    histogram, bins = np.histogram(img, bins=256, range=(0, 1))
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    ret,thresh = cv2.threshold(img,85,255,cv2.THRESH_TOZERO)
    #th, thresh = cv2.threshold(img, 128, 192, cv2.THRESH_OTSU)

    #plt.hist(gray_img.ravel(),256,[0,256])
    #plt.plot(bins[0:-1],histogram)
    #plt.title('Histogram for gray scale picture')
    #plt.show()

    cv2.namedWindow("Threshold", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Threshold', 640, 640)
    cv2.imshow('Threshold', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.namedWindow("Laplacian", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Laplacian', 640, 640)
    cv2.imshow('Laplacian', np.uint8(np.absolute(laplacian)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    del img, gray_img, laplacian, thresh


