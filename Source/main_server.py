
import cv2

from time import sleep
import threading as thr
import logging as log

import config as cfg

from camera import Camera as cam
from server.recognizer import Recognizer as rec
from server.server import Server
from gpio.gpio import GPIO as GPIO


# Wierd helpers

def find_x_center(points):
    if len(points) == 1:
        return points[0][0]
    else:
        minimum = min(points)[0]
        maximum = max(points)[0]
        return (minimum + maximum) // 2


def start_server_thread(name, container):
    log.info(f"Server - Starting server in a daemon thread {name} ....")
    Server(ip=cfg.HOST_IP, port=cfg.HOST_PORT, container=container)


if __name__ == "__main__":
    log.info("Server - initialising...")

    if not cfg.IF_IN_RPI:
        log.warning("Server - Not in RPi. Emulating work with GPIO.")

    if cfg.LOAD_STREAM:
        log.info("Server - Streaming video from rtsp ip camera.")
        device = cfg.STREAM_RTSP_IP
    else:
        log.info("Server - Streaming video from embedded web camera")
        device = cfg.STREAM_WEB_ID

    container = []

    x = thr.Thread(target=start_server_thread,
                   args=(1, container),
                   daemon=True)
    x.start()

    log.info("NEXT")

    try:
        while True:
            sleep(2)
            log.info(f"{len(container)}")
    except KeyboardInterrupt:
        log.error("Server - KeyboardInterrupt")

    # cam = cam(device=device)
    # rec = rec()
    # gpio = GPIO()

    # while True:
    #     ret, frame = cam.read_frame()

    #     frame_modified = rec.filter_frame(frame)
    #     frame, center_list = rec.detect(frame)

    #     # LEDs
    #     if center_list:
    #         gpio.signal_led.turn_on()
    #         gpio.buzzer.turn_on()
    #     else:
    #         gpio.signal_led.turn_off()
    #         gpio.buzzer.turn_off()

    #     # Servo
    #     if center_list:
    #         center = find_x_center(center_list)
    #         cv2.circle(frame,
    #                    (center, frame.shape[0] // 2),
    #                    cfg.DRAW_CENTER_RADIUS,
    #                    cfg.DRAW_COLOR_GREEN,
    #                    cfg.DRAW_CIRCLE_THICKNESS)

    #     cv2.imshow(cfg.WINDOW_ORIGINAL_IMAGE, frame)
    #     cv2.imshow(cfg.WINDOW_MODIFIED_IMAGE, frame_modified)

    #     if cv2.waitKey(cfg.WAIT_KEY_TIME) == ord(cfg.WAIT_KEY):
    #         break

    # cv2.destroyAllWindows()
