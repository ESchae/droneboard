import cv2
import numpy as np
import util

def detect_circles(frame, lower, upper, windowname = "detect circles"):
    """
    detect_circles uses the hough transform 
    to detect circles (-> the control knobs)

    Returns
    -------

    All found circles 

    """
    # BGR -> HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # threshold to get only color between 'lower' and 'upper'
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise AND mask 
    res = cv2.bitwise_and(frame, frame, mask=mask)


    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)

    circles = cv2.HoughCircles(gray,
                               cv2.HOUGH_GRADIENT,
                               1,
                               20, 
                               param1=50,    # 50
                               param2=10,    # 30
                               minRadius=3,
                               maxRadius=50)


    if type(circles) == np.ndarray:
        circles = np.uint16(np.around(circles))
        util.draw_circles(frame, windowname, circles)

        return circles

    return []

