import os
import cv2
from src.utils import display_image
from src.constants import GRID_SIZE
import numpy as np

def grid_detection(*args):
    '''
    The function detects the grid in the image

    input:
    args[0]- input image (array like numpy),
    args[1]- manually selected grid size in the image (integer)

    output:
    output- output image with detected rectangular grid (array like numpy)
    '''
    if len(args)==0:
        raise SyntaxError('You should input one argument at least!')
    elif len(args)==1:
        gray_img = args[0]

        blurred = cv2.medianBlur(gray_img, 25)
        #th, thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_OTSU)
        th, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_OTSU)
        laplacian = cv2.Laplacian(thresh, cv2.CV_64F, ksize=5)
        edges=np.uint8(np.absolute(laplacian))
        output = gray_img.copy() #np.uint8(np.absolute(laplacian))

        param1 =250 #250 500
        param2 =30 #44 200 #smaller value-> more false circles
        minRadius = 800
        maxRadius = 1000 #10
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
        #print(circles)

        # ensure at least some circles were found
        crop_range=[]
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            (x, y, r) = circles[0]
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            #cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - r//2, y - r//2), (x + r//2, y + r//2), (0, 255, 0), 5)
            crop_range = [(x - r//2, y - r//2), (x + r//2, y + r//2)]
        else:
            img_size = np.shape(gray_img)
            half_size = min(img_size)//6
            x, y = img_size[1]//2, img_size[0]//2
            crop_range = [(x - half_size, y - half_size), (x + half_size, y + half_size)]
            cv2.rectangle(output, crop_range[0], crop_range[1], (0, 255, 0), 5)

    elif len(args)>1:
        gray_img = args[0]
        half_size = args[1]//2
        img_size = np.shape(gray_img)
        x, y = img_size[1]//2, img_size[0]//2

        output = gray_img.copy()
        crop_range = [(x - half_size, y - half_size), (x + half_size, y + half_size)]
        cv2.rectangle(output, crop_range[0], crop_range[1], (0, 255, 0), 5)

    return output, crop_range

if __name__=="__main__":
    images_dir_path = r'/home/soul/Downloads/dfdf-05-21-2021_09_23_50_PM.tiff'
    #filenames=os.listdir(images_dir_path)
    #img_path=os.path.join(images_dir_path, filenames[0])

    gray_img=cv2.imread(images_dir_path,0)

    output_img, crop_range = grid_detection(gray_img)
    display_image(output_img, 'Detected Grid', (640,640), 0)
