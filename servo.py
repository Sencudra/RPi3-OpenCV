
import config as cfg
from time import sleep

if cfg.IF_IN_RPI:
    import RPi.GPIO as GPIO


class SERVO:
    def __init__(self, pin):
        """
            Should be carefull while initialising Servos. No checks here.
        """
        print(f"Configuring SERVO pin: {pin}.")
        self.pin = pin
        self.angle = 0

        if cfg.IF_IN_RPI:
            GPIO.setup(pin, GPIO.OUT)
            self.pwm = GPIO.PWM(pin, cfg.SERVO_FREQUENCY)
            self.pwm.start(0)
            print("Setting angle to 0")
            self.set_angle(0)

    def set_angle(self, angle):
        # some magic here idk
        print(f"Setting angle {self.angle}")

        if cfg.IF_IN_RPI:
            duty = angle / 18 + 2
            GPIO.output(self.pin, True)
            self.pwm.ChangeDutyCycle(duty)
            sleep(1)
            GPIO.output(self.pin, False)
            self.pwm.ChangeDutyCycle(duty)
