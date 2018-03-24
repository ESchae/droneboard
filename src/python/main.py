import numpy as np
import cv2
import math

import control_knob
import detect_whiteboard 
import util


def main_loop():
    webcam = 0
    frame_counter = 0
    margin_whiteboard = []
    cap = cv2.VideoCapture(webcam)

    # extract whiteboard
    for l in range(0,300):
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
    

    while(1):
        # Take each frame
        _, frame = cap.read()
        frame = frame[ymin:ymax, xmin:xmax]

        # blue range in HSV
        lower_blue = np.array([80,50,50])
        upper_blue = np.array([130,255,255])

        lower_brown = np.array([10, 100, 20])
        upper_brown = np.array([20, 255, 200])

        s = 15
        lower_red = np.array([170-s,70,30])
        upper_red = np.array([180+s,255,255])

        if frame_counter % 5 == 0:
            circles_blue = control_knob.detect_circles(frame, lower_blue, upper_blue)


        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

        frame_counter += 1

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main_loop()




