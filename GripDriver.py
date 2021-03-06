
import cv2
import numpy as np
from pleasework import PleaseWork
from networktables import NetworkTables
NetworkTables.initialize(server='10.62.39.2')
rp= NetworkTables.getTable("Camera2")

grip = PleaseWork()
print(cv2.__version__)
# cap = cv2.VideoCapture("http://192.168.2.2:1181/stream.mjpg")
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    grip.process(frame)
   # cv2.drawContours(frame, grip.filter_contours_output, cv2.FILLED, (10, 0, 255), 2)

    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 215, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    # cMax = max(contours, key = cv2.contourArea) python's indent system is crap :)

    if(len(contours) > 0):

        cMax = max(contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(cMax)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], cv2.FILLED, (255, 0, 100), 3)

        circleRect = cv2.boundingRect(cMax)
        x, y, w, h = circleRect
        xCent = int(x+(w/2))
        yCent = int(y+(h/2))
        cv2.circle(img,(xCent, yCent), 5, (0,255,0), 2)
      
        rp.putNumber("xDiff", 320-xCent)
        rp.putNumber("yDiff",180-yCent)


            # x, y, w, h = rect
      	    # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img



        cv2.imshow('frame', img)
        # cv2.waitKey(60)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
