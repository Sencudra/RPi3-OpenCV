
import config as cfg

from gpio.led import LED as LED
from gpio.servo import SERVO as SERVO
from gpio.buzzer import Buzzer as Buzzer
from gpio.distance_sensor import DistanceSensor as DS

if cfg.IF_IN_RPI:
    import RPi.GPIO


class GPIO:
    def __init__(self):
        print("GPIO configuring.")

        if cfg.IF_IN_RPI:
            RPi.GPIO.setmode(RPi.GPIO.BCM)

        # GPIO initialization
        self.signal_led = LED(pin=cfg.LED_PIN)
        self.servo = SERVO(pin=cfg.SERVO_PIN)
        self.buzzer = Buzzer(pin=cfg.BUZZER_PIN)
        self.distance_sensor = DS(echo_pin=cfg.DISTANCE_SENSOR_ECHO_PIN,
                                  trig_pin=cfg.DISTANCE_SENSOR_TRIG_PIN)

    def __del__(self):
        print("GPIO cleaning.")
        if cfg.IF_IN_RPI:
            RPi.GPIO.cleanup()
