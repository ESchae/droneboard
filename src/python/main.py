import numpy as np
import cv2
import math

import control_knob
import detect_whiteboard 
import util
import logging

logging.basicConfig(level=logging.DEBUG)

from whiteboard import Whiteboard

wb = Whiteboard()

def circles2dict(circles, width, height, id_, rotation):
    if type(circles) != np.ndarray:
        return []

    circle_dict = []
    for c in circles[0,:]:
        circle_dict.append({"id": id_, "x":c[0]/width, "y":c[1]/height, "rotation":rotation})
    return circle_dict


def main_loop():
    webcam = 0
    frame_counter = 0
    margin_whiteboard = []
    cap = cv2.VideoCapture(webcam)

    # extract whiteboard
    for l in range(0,100):
        _, frame = cap.read()
        c = detect_whiteboard.detect_whiteboard(frame)
        margin_whiteboard += c

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cluster = detect_whiteboard.corners(margin_whiteboard)
    p1 = list(map(math.floor, cluster[0]))
    p2 = list(map(math.floor, cluster[1]))
 
    xmin, xmax = sorted([p1[0],p2[0]])
    ymin, ymax = sorted([p1[1],p2[1]])
    w = xmax - xmin
    h = ymax - ymin
    eps = 10

    while(1):
        # Take each frame
        _, frame = cap.read()
        frame = frame[ymin-eps:ymax+eps, xmin+eps:xmax-eps]

        # blue range in HSV
        lower_blue = np.array([80,50,50])
        upper_blue = np.array([130,255,255])

        lower_brown = np.array([10, 100, 20])
        upper_brown = np.array([20, 255, 200])

        lower_yellow = np.array([20,100,100])
        upper_yellow = np.array([30,255,255])

        s = 15
        lower_red = np.array([170-s,70,30])
        upper_red = np.array([180+s,255,255])

        lower_green = np.array([65,60,60])
        upper_green = np.array([80,255,255])

        if frame_counter % 5 == 0:
            circles_blue = control_knob.detect_circles(frame, lower_blue, upper_blue)
            circles_red = control_knob.detect_circles(frame, lower_red, upper_red)
            circles_yellow = control_knob.detect_circles(frame, lower_yellow, upper_yellow)
            circles_green = control_knob.detect_circles(frame, lower_green, upper_green)
            

            c = circles2dict(circles_blue, w, h, 1, 0.5) + circles2dict(circles_red, w, h, 0, 0.5) +  \
            circles2dict(circles_yellow, w, h, 2, 0.5) + circles2dict(circles_green, w, h, 3, 0.5)
            
            wb.update(c)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

        frame_counter += 1

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main_loop()




