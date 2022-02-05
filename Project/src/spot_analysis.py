import os
import cv2
import numpy as np
from src.utils import display_image

def spot_analysis(gray_img):   
    #gray_img = cv2.medianBlur(gray_img, 25)
    output = gray_img.copy()
    ret,thresh = cv2.threshold(gray_img,70,255,cv2.THRESH_TOZERO)
    #cv2.imshow('Image', thresh)
    # detect circles in the image
    param1 = 10 #500
    param2 = 15 #200 #smaller value-> more false circles
    minRadius = 5
    maxRadius = 15 #10
    circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 50, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    num_circles = 0
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            #cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            num_circles+=1
                    
    return output, num_circles

if __name__=="__main__":
    path = r'/home/soul/Desktop/ProjectSpotAnalysis/Project/images/Good/whiteboxe0f4.tiff'

    filenames = path
    #filenames=os.listdir('/home/soul/Desktop/ProjectSpotAnalysis/Project/images/Good')[1]
    #img_path=os.path.join(images_dir_path, filenames[1])

    gray_img=cv2.imread(filenames,0)
    

    IMG_SIZE = np.shape(gray_img)
    #MARGIN_WIDTH = [round(IMG_SIZE[1]/4.5), round(IMG_SIZE[1]/4)]
    #MARGIN_HEIGHT = [round(IMG_SIZE[0]/5), round(IMG_SIZE[0]/5)]
    #gray_img = gray_img[MARGIN_HEIGHT[0]:-MARGIN_HEIGHT[1],MARGIN_WIDTH[0]:-MARGIN_WIDTH[1]]
    output_img, num_circles=spot_analysis(gray_img)
    print(num_circles)

    display_image(output_img, 'Detected circles', (640,640), 0)
    