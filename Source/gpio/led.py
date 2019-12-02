
import logging as log
import config as cfg

if cfg.IF_IN_RPI:
    import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin):
        """
            Should be carefull while initialising LEDs. No checks here.
        """
        self.pin = pin
        self.mode = False
        log.info("LED - Initialising. Pin used: {pin}.".format(pin=self.pin))
    
        if cfg.IF_IN_RPI:
            GPIO.setup(self.pin, GPIO.OUT)

    def turn_on(self):
        if not self.mode:
            self.mode = not self.mode
            log.info("LED - {pin} is on".format(pin=self.pin))
            if cfg.IF_IN_RPI:
                GPIO.output(self.pin, True)

    def turn_off(self):
        if self.mode:
            self.mode = not self.mode
            log.info("LED - {pin} is off".format(pin=self.pin))
            if cfg.IF_IN_RPI:
                GPIO.output(self.pin, False)
