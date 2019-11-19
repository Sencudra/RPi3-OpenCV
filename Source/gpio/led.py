
import config as cfg

if cfg.IF_IN_RPI:
    import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin):
        """
            Should be carefull while initialising LEDs. No checks here.
        """
        print(f"LED pin configuring: {pin}.")
        self.pin = pin
        self.mode = False

        if cfg.IF_IN_RPI:
            GPIO.setup(pin, GPIO.OUT)

    def turn_on(self):
        if not self.mode:
            self.mode = not self.mode
            print(f"LED {self.pin} is on!")
            if cfg.IF_IN_RPI:
                print("RPI on")
                GPIO.output(self.pin, True)

    def turn_off(self):
        if self.mode:
            self.mode = not self.mode
            print(f"LED {self.pin} is off!")
            if cfg.IF_IN_RPI:
                GPIO.output(self.pin, False)
