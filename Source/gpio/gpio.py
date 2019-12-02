
import logging as log
import config as cfg

if cfg.IF_IN_RPI:
    import RPi.GPIO


class GPIO:

    signal_led = None
    buzzer = None
    distance_sensor = None
    servo = None

    def __init__(self):
        log.info("GPIO - Initialising...")

        if cfg.IF_IN_RPI:
            RPi.GPIO.setmode(RPi.GPIO.BCM)

    def __del__(self):
        log.info("GPIO - Cleaning...")

        if cfg.IF_IN_RPI:
            RPi.GPIO.cleanup()
