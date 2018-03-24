import cv2

def draw_circles(frame, window_name, circles):

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)


    #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, frame)
 

