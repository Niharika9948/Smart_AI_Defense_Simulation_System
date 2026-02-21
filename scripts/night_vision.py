import cv2

def night_vision(frame):
    """
    Simulate night vision effect by enhancing green channel.
    """
    green = frame[:,:,1]
    frame[:,:,0] = 0  # remove blue
    frame[:,:,2] = 0  # remove red
    frame[:,:,1] = cv2.add(green, 50)  # enhance green channel
    return frame