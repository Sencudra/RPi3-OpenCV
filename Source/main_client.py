
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

    client = Client(to_ip=cfg.HOST_IP,
                    with_port=cfg.HOST_PORT)

    try:
        old_distance = None
        while True:
            distance = gpio.distance_sensor.get_distance()

            if distance != old_distance:
                client.send_data(distance)
                old_distance = distance
                gpio.signal_led.turn_on()
                sleep(1)
                gpio.signal_led.turn_off()
            else:
                sleep(1)
    except KeyboardInterrupt:
        log.error("Client - KeyboardInterrupt")
        pass
