
import cv2
import logging as log


class Camera:

    def __init__(self, device=0):
        log.info("Camera - Initiailsing...")
        self.cam = cv2.VideoCapture(device)
        log.info("Camera - Initialized.")

    def __del__(self):
        log.info("Camera - Releasing...")
        self.cam.release()

    def read_frame(self):
        return self.cam.read()
