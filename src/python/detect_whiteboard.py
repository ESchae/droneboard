import cv2
import numpy as np
from sklearn.cluster import KMeans

import control_knob
import util

def corners(coordinates):
    """
    use k-means (with ``K=2``) in order to get the lower left 
    and upper right corner of the whiteboard

    Params
    ------
    coordinates:  

    """
    kmeans = KMeans(n_clusters=2, random_state=0).fit(coordinates)
    return kmeans.cluster_centers_


def detect_whiteboard(frame):
    """
    detect_whiteboard extracts the margin of the whiteboard
    using special makers...

    Params
    ------
    frame

    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    s = 15
    lower_red = np.array([170-s,70,30])
    upper_red = np.array([180+s,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise AND mask -- original image
    whiteboard = cv2.bitwise_and(frame,frame, mask=mask)

    circles = control_knob.detect_circles(whiteboard, lower_red, upper_red, "whiteboard margin")

    if type(circles) != np.ndarray:
        return []

    circles_coords = [[xy[0], xy[1]] for xy in circles[0,:]]

    return circles_coords

