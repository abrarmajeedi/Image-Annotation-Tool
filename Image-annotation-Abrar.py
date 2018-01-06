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
        df.to_csv(str(file[0])+".csv", header=False, index=False)

        
def click_record(event, x, y, flags, param):
        global refPt
        # if the left mouse button was clicked, record the (x, y) coordinates 
        if event == cv2.EVENT_LBUTTONDOWN:
                refPt = (x, y)
                points.append(refPt)

count = int(input("Which file do you want to start with?\n"))

D= dict()
for file in os.listdir(os.getcwd()):
    ext_temp = file.split("_")[-1]
    
    file_ext =  file.split(".")[-1]
    if file == "scr.py" or file_ext == "csv":
        continue
    number = int(ext_temp.split(".")[0])
    D[number] = file

for key in sorted(D.keys()):
        file = D[key]
        ext_temp = file.split("_")[-1]
        number = int(ext_temp.split(".")[0])
        file_ext =  file.split(".")[-1]
        
        
        if number < count :
                continue
        # load the image, and setup the mouse callback function
        image = cv2.imread(os.getcwd()+"\\"+str(file))
        cv2.namedWindow("image",flags = cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('image', 600,600)
        cv2.setMouseCallback("image", click_record)


        while True:
                # display the image and wait for a keypress
                 cv2.imshow("image", image)
                 key = cv2.waitKey(1) & 0xFF
                 if key == ord("n"):
                         break
                 if key == ord("r"):
                         points = []
                        
                 if key == ord("q"):
                         cv2.waitKey(0)
                         cv2.destroyAllWindows()
                         quit()
                 if key == ord('e'):
                         cv2.line(image, points[0],points[1],(0,255,0), 1)
                         cv2.line(image, points[1],points[2],(0,255,0), 1)
                         cv2.line(image, points[2],points[3],(0,255,0), 1)
                         cv2.line(image, points[0],points[4],(0,255,0), 1)
                         cv2.line(image, points[0],points[5],(0,255,0), 1)
                         cv2.line(image, points[1],points[5],(0,255,0), 1)
                         cv2.line(image, points[1],points[6],(0,255,0), 1)
                         cv2.line(image, points[2],points[7],(0,255,0), 1)
                         cv2.line(image, points[2],points[8],(0,255,0), 1)
                         cv2.line(image, points[3],points[8],(0,255,0), 1)
                         cv2.line(image, points[3],points[9],(0,255,0), 1)
                         cv2.line(image, points[3],points[11],(0,255,0), 1)
                         cv2.line(image, points[0],points[10],(0,255,0), 1)
                         cv2.line(image, points[5],points[12],(0,255,0), 1)
                         cv2.line(image, points[6],points[13],(0,255,0), 1)
                         cv2.line(image, points[7],points[13],(0,255,0), 1)
                         cv2.line(image, points[8],points[14],(0,255,0), 1)
                         cv2.line(image, points[12],points[13],(0,255,0), 1)
                         cv2.line(image, points[13],points[14],(0,255,0), 1)
                         cv2.line(image, points[12],points[15],(0,255,0), 1)
                         cv2.line(image, points[14],points[17],(0,255,0), 1)
                         cv2.line(image, points[15],points[16],(0,255,0), 1)
                         cv2.line(image, points[16],points[17],(0,255,0), 1)
                         cv2.line(image, points[15],points[18],(0,255,0), 1)
                         cv2.line(image, points[17],points[19],(0,255,0), 1)
                         cv2.line(image, points[4],points[10],(0,255,0), 1)
                         cv2.line(image, points[9],points[11],(0,255,0), 1)
                         cv2.line(image, points[10],points[18],(0,255,0), 1)
                         cv2.line(image, points[11],points[19],(0,255,0), 1)
                         cv2.line(image, points[18],points[19],(0,255,0), 1)
                         cv2.circle(image,points[0], 3, (0,0,255), -1)
                         cv2.circle(image,points[1], 3, (0,0,255), -1)
                         cv2.circle(image,points[2], 3, (0,0,255), -1)
                         cv2.circle(image,points[3], 3, (0,0,255), -1)
                         cv2.circle(image,points[4], 3, (0,0,255), -1)
                         cv2.circle(image,points[5], 3, (0,0,255), -1)
                         cv2.circle(image,points[6], 3, (0,0,255), -1)
                         cv2.circle(image,points[7], 3, (0,0,255), -1)
                         cv2.circle(image,points[8], 3, (0,0,255), -1)
                         cv2.circle(image,points[9], 3, (0,0,255), -1)
                         cv2.circle(image,points[10], 3, (0,0,255), -1)
                         cv2.circle(image,points[11], 3, (0,0,255), -1)
                         cv2.circle(image,points[12], 3, (0,0,255), -1)
                         cv2.circle(image,points[13], 3, (0,0,255), -1)
                         cv2.circle(image,points[14], 3, (0,0,255), -1)
                         cv2.circle(image,points[15], 3, (0,0,255), -1)
                         cv2.circle(image,points[16], 3, (0,0,255), -1)
                         cv2.circle(image,points[17], 3, (0,0,255), -1)
                         cv2.circle(image,points[18], 3, (0,0,255), -1)
                         cv2.circle(image,points[19], 3, (0,0,255), -1)
                         
        if len(points) > 20:
                 quit()
        save_data(points,str(file))
        
        points = []
        cv2.waitKey(0)
        cv2.destroyAllWindows()










