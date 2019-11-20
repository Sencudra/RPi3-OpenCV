
import time
import logging as log

import config as cfg

if cfg.IF_IN_RPI:
    import RPi.GPIO as GPIO


class Buzzer:
    def __init__(self, pin):
        """
            Should be carefull while initialising PIs. No checks here.
        """
        log.info(f"Buzzer - Initialising. Pin used: {pin}.")
        self.pin = pin
        self.mode = False

        if cfg.IF_IN_RPI:
            GPIO.setup(pin, GPIO.OUT)
            self.pwm = GPIO.PWM(pin, cfg.BUZZER_DEFAULT_FREQUENCY)
            self.pwm.start(0)

    def __del__(self):
        log.info("Buzzer - Cleaning...")
        if cfg.IF_IN_RPI:
            self.pwm.stop()

    def change_pitch(self, percent):
        number = percent
        if number > 100:
            number = 100
        elif number < 0:
            number = 0

        log.info("Buzzer - Changing Frequency")
        self.pwm.ChangeFrequency(percent / 100 * 22000)

    def turn_on(self):
        if not self.mode:
            self.mode = not self.mode
            log.info(f"Buzzer - {self.pin} is on")
            if cfg.IF_IN_RPI:
                self.pwm.start(70)

    def turn_off(self):
        if self.mode:
            self.mode = not self.mode
            log.info(f"Buzzer - {self.pin} is off")
            if cfg.IF_IN_RPI:
                self.pwm.start(0)


if __name__ == "__main__":
    """
        Temp Test
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 100)

    c4 = 261
    d4 = 294
    e4 = 329
    f4 = 349
    g4 = 392
    a4 = 440
    b4 = 493
    c5 = 523.25

    speed = 0.1

    GPIO.output(12, True)
    p.start(10)

    while True:
        p.ChangeFrequency(c4)
        time.sleep(speed)
        p.ChangeFrequency(d4)
        time.sleep(speed)
        p.ChangeFrequency(e4)
        time.sleep(speed)
        p.ChangeFrequency(f4)
        time.sleep(speed)
        p.ChangeFrequency(g4)
        time.sleep(speed)
        p.ChangeFrequency(a4)
        time.sleep(speed)
        p.ChangeFrequency(b4)
        time.sleep(speed)
        p.ChangeFrequency(c5)
        time.sleep(speed)

    p.stop()
    GPIO.cleanup()
