from src.spot_analysis import spot_analysis
from src.grid_detection import grid_detection
from src.utils import *
from src.constants import *
import os
import shutil
import cv2
path = r'/home/soul/Desktop/ProjectSpotAnalysis/Project/images/Bad'

l = os.listdir(path)

for i in l:
    
    img_path = os.path.join(path,i)
    

    gray_img=cv2.imread(img_path,0)   
    _, crop_range = grid_detection(gray_img)
    cropped_img=crop_image(gray_img, crop_range)
    output_img, num_circles=spot_analysis(cropped_img)   

    print(num_circles)
#cv2.imshow('Image',output_img)
        # make sure if the image is too bright
    IsTooBright = False
#BrightPixels=cropped_img[cropped_img>BRIGHT_THRES]
    BrightPixels=cropped_img[cropped_img>BRIGHT_THRES]
    IsTooBright = len(BrightPixels)>500
        #print(IsTooBright)
    if num_circles>6 and num_circles<30 and not IsTooBright:
        target_path=os.path.join(OUTPUT_PATH, 'Good')
          
        alert=img_path+' is GOOD image'
        print(alert)
        print('\tnumber of detected circles: %d'%(num_circles))        
    else:
        target_path=os.path.join(OUTPUT_PATH, 'Bad')

        alert=img_path+' is BAD image'
        print(alert) 

#shutil.copy(img_path,os.path.join(target_path, img_path))
#cv2.putText(output_img,alert,(10,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)
#display_image(output_img, 'Detected circles', (640,640), 0)
