# Python program to illustrate HoughLine
# method for line detection
import numpy as np
import cv2
print(cv2.__version__)
cap = cv2.VideoCapture(0)


while(cap.isOpened()):
    ret, frame = cap.read()

    img = frame
# Convert the img to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   # cv2.imwrite('gray.jpg', gray)

# Apply edge detection method on the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
  #  cv2.imwrite('edges.jpg', edges)

# This returns an array of r and theta values

    lines = cv2.HoughLines(edges, 1, np.pi/180, 150)
#  i = 0
# idontknowhowtouseforloopsinpython = (len(lines));
# The below for loop runs till r and theta values
# are in the range of the 2d array

#   while(i < idontknowhowtouseforloopsinpython):
    if lines is not None:
       for line in lines:
        for r, theta in line:

                                    # Stores the value of cos(theta) in a
            a = np.cos(theta)

                                    # Stores the value of sin(theta) in b
            b = np.sin(theta)

                                    # x0 stores the value rcos(theta)
            x0 = a*r

                                    # y0 stores the value rsin(theta)
            y0 = b*r

                                    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
            x1 = int(x0 + 1000*(-b))

                                    # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
            y1 = int(y0 + 1000*(a))

                                    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
            x2 = int(x0 - 1000*(-b))

                                    # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
            y2 = int(y0 - 1000*(a))

                                    # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
                                    # (0,0,255) denotes the colour of the line to be
                                    # drawn. In this case, it is red.
            cv2.line(img, (x1, y1), (x2, y2),(0, 0, 255), 2)
                                    #       i+=1
                                    # print(i)
                                    # All the changes made in the input image are finally
                                    # written on a new image houghlines.jpg
                            #  cv2.imwrite("foundLine.jpg", img)
    cv2.imshow('frame', img)
    cv2.waitKey(30)
        
