
import logging as log
from time import sleep

import config as cfg

from client.client import Client
from gpio.gpio import GPIO
from gpio.led import LED as LED
from gpio.distance_sensor import DistanceSensor as DS


if __name__ == "__main__":

    log.info("Client - initialising...")

    if not cfg.IF_IN_RPI:
        log.warning("Client - Not in RPi. Emulating work with GPIO.")

    gpio = GPIO()
    gpio.signal_led = LED(pin=cfg.LED_PIN)
    gpio.distance_sensor = DS(echo_pin=cfg.DISTANCE_SENSOR_ECHO_PIN,
                              trig_pin=cfg.DISTANCE_SENSOR_TRIG_PIN)

    client = Client()

    try:
        old_distance = None
        while True:
            distance = gpio.distance_sensor.get_distance()

            if distance != old_distance:
                client.send_data(distance,
                                 cfg.HOST_IP,
                                 cfg.HOST_PORT)
                old_distance = distance
                gpio.signal_led.turn_on()
                sleep(0.2)
                gpio.signal_led.turn_off()
            else:
                sleep(1)
    except KeyboardInterrupt as e:
        log.info(e)
        pass
