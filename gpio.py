
import config as cfg

from led import LED as LED
from servo import SERVO as SERVO
from pi import PI as PI

if cfg.IF_IN_RPI:
    import RPi.GPIO


class GPIO:
    def __init__(self):
        print("Configuring GPIO.")

        if cfg.IF_IN_RPI:
            RPi.GPIO.setmode(RPi.GPIO.BCM)

        # GPIO initialization
        self.signal_led = LED(pin=cfg.LED_PIN)
        self.servo = SERVO(pin=cfg.SERVO_PIN)
        self.pi = PI(pin=8)

    def __del__(self):
        if cfg.IF_IN_RPI:
            RPi.GPIO.cleanup()
        else:
            print("Cleaning GPIO.")
