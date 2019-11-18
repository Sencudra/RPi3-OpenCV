
import config as cfg

if cfg.IF_IN_RPI:
    import RPi.GPIO as GPIO


class PI:
    def __init__(self, pin):
        """
            Should be carefull while initialising PIs. No checks here.
        """
        print(f"Configuring Pi pin: {pin}.")
        self.pin = pin
        self.mode = False
        
        if cfg.IF_IN_RPI:
            GPIO.setup(pin, GPIO.OUT)
            self.pwm = GPIO.PWM(pin, 15000)
            self.pwm.start(0)
            
    def __del__(self):
        self.pwm.stop()
            
    def change_pitch(percent):
        number = percent
        if number > 100:
            number = 100
        elif number < 0:
            number = 0
        
        print("Changing Frequency")
        self.pwm.ChangeFrequency(percent / 100 * 20000)

    def turn_on(self):
        if not self.mode:
            self.mode = not self.mode
            print(f"Pi {self.pin} is on!")
            if cfg.IF_IN_RPI:
                self.pwm.start(70)
                #GPIO.output(self.pin, True)

    def turn_off(self):
        if self.mode:
            self.mode = not self.mode
            print(f"Pi {self.pin} is off!")
            if cfg.IF_IN_RPI:
                self.pwm.start(0)
                #GPIO.output(self.pin, False)

