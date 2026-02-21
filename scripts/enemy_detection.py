import cv2
import numpy as np

def detect_enemies(frame):
    """
    Detect enemies based on red color in frame.
    Returns frame with bounding boxes and list of enemy coordinates.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Red color ranges
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    enemies = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w*h > 500:  # ignore small noise
            enemies.append((x, y, w, h))
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    return frame, enemies