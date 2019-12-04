
import cv2

import threading as thr
import logging as log

import config as cfg

from camera import Camera as cam
from server.recognizer import Recognizer as rec
from server.server import Server

from gpio.gpio import GPIO
from gpio.buzzer import Buzzer
from gpio.led import LED
from gpio.servo import Servo


# Wierd helpers

def find_x_center(points):
    if len(points) == 1:
        return points[0][0]
    else:
        minimum = min(points)[0]
        maximum = max(points)[0]
        return (minimum + maximum) // 2


def start_server_thread(name, server):
    log.info("Server - Starting server in a daemon thread {name}".format(
        name=name
    ))
    server.start()


def distance_to_percent(distance):
    percent = abs(1 - distance / cfg.DUSTANCE_SENSOR_MAX * 100)
    log.info("Server - Distance percent calculated {percent}".format(
        percent=percent
    ))
    return percent


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

    cam = cam(device=device)
    rec = rec()

    gpio = GPIO()
    gpio.signal_led = LED(pin=cfg.LED_PIN)
    gpio.buzzer = Buzzer(pin=cfg.BUZZER_PIN)
    gpio.buzzer.turn_on()
    gpio.servo = Servo(pin=cfg.SERVO_PIN)

    s = Server(ip=cfg.HOST_IP, port=cfg.HOST_PORT, container=container)
    thr.Thread(target=start_server_thread,
               args=(1, s),
               daemon=True).start()

    log.info("NEXT")

    try:
        while True:
            ret, frame = cam.read_frame()

            frame_modified = rec.filter_frame(frame)
            frame, center_list = rec.detect(frame)

            # Buzzer
            if container:
                distance = int(container.pop())
                percent = distance_to_percent(distance)
                gpio.buzzer.change_loudness(percent)

            # LEDs
            if center_list:
                gpio.signal_led.turn_on()
            else:
                gpio.signal_led.turn_off()

            # Servo
            if center_list:
                center = find_x_center(center_list)
                x = frame.shape[1] // 2 - center

                direction = None
                if x > 0:
                    direction = -5
                elif x < 0:
                    direction = 5
                else:
                    direction = 0

                gpio.servo.set_angle(gpio.servo.angle + direction)

            cv2.imshow(cfg.WINDOW_ORIGINAL_IMAGE, frame)
            cv2.imshow(cfg.WINDOW_MODIFIED_IMAGE, frame_modified)

            if cv2.waitKey(cfg.WAIT_KEY_TIME) == ord(cfg.WAIT_KEY):
                break

    except KeyboardInterrupt:
        log.error("Server - KeyboardInterrupt")

    cv2.destroyAllWindows()
