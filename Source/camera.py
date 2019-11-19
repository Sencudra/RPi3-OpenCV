
import cv2


class Camera:

    def __init__(self, device=0):
        print("Initiailsing camera!")
        self.cam = cv2.VideoCapture(device)
        print("camera initialized!")

    def __del__(self):
        self.cam.release()

    def read_frame(self):
        return self.cam.read()
