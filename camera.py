
import cv2


class Camera:

    def __init__(self, device=0):
        self.cam = cv2.VideoCapture(device)

    def __del__(self):
        self.cam.release()

    def read_frame(self):
        return self.cam.read()
