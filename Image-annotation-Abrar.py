"""Author: Abrar A. Majeedi
      Date: 27/12/2017
      Place: Indian Institute of Science, Bangalore"""


import cv2
import os
import numpy as np
import pandas as pd 
result = []
points = []
refPt = ()


def save_data(result,file):
        a = np.asarray(result)
        df = pd.DataFrame(a)
        file = file.split(".")
        df.to_csv(str(file[0])+".csv" )

        
def click_record(event, x, y, flags, param):
        global refPt
        # if the left mouse button was clicked, record the (x, y) coordinates 
        if event == cv2.EVENT_LBUTTONDOWN:
                refPt = (x, y)
                points.append(refPt)

for file in os.listdir("Path"):
        # load the image, and setup the mouse callback function
        image = cv2.imread("Path"+str(file))
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_record)
 

        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
           
 
        # if the 'c' key is pressed, break from the loop
        if key == ord("c"):
                cv2.waitKey(0)
                cv2.destroyAllWindows()


        while True:
                # display the image and wait for a keypress
                 cv2.imshow("image", image)
                 key = cv2.waitKey(1) & 0xFF
                 if key == ord("n"):
                         break
                 if key == ord("r"):
                         points = []
                        
                 if key == ord("q"):
                         save_data(result)
                         quit()
                 
        temp = []
        for i in points:
                l = list(i)
                l.append(file)
                temp.append(l)
                
        save_data(temp,file)
        
        points = []
        cv2.waitKey(0)
        cv2.destroyAllWindows()





