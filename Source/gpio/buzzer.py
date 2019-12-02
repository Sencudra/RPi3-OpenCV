
import logging as log
import config as cfg

if cfg.IF_IN_RPI:
    import RPi.GPIO as GPIO


class Buzzer:
    def __init__(self, pin):
        """
            Should be carefull while initialising PIs. No checks here.
        """
        log.info("Buzzer - Initialising. Pin used: {pin}.".format(pin=pin))
        self.pin = pin
        self.mode = False
        self.loudness = 100

        if cfg.IF_IN_RPI:
            GPIO.setup(pin, GPIO.OUT)
            self.pwm = GPIO.PWM(pin, cfg.BUZZER_DEFAULT_FREQUENCY)
            self.pwm.start(100)

    def __del__(self):
        log.info("Buzzer - Cleaning...")
        if cfg.IF_IN_RPI:
            self.pwm.stop()

    def change_loudness(self, percent):
        log.info("Buzzer - Loudness {percent}%".format(percent=percent))
        if cfg.IF_IN_RPI:
            self.__setVolume(percent)

    def turn_on(self):
        if not self.mode:
            self.mode = not self.mode
            log.info("Buzzer - {pin} is on".format(pin=self.pin))
            if cfg.IF_IN_RPI:
                self.__setVolume(100)

    def turn_off(self):
        if self.mode:
            self.mode = not self.mode
            log.info("Buzzer - {pin} is off".format(pin=self.pin))
            if cfg.IF_IN_RPI:
                self.__setVolume(0)

    def __setVolume(self, percent):
        loudness = None
        if percent > 100:
            loudness = 100
        elif percent < 0:
            loudness = 0
        else:
            loudness = percent
        self.loudness = loudness
        self.pwm.start(float(self.loudness))
        log.info("Buzzer - Loudness is {loudness}".format(loudness=self.loudness))
