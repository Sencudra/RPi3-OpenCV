
import config as cfg

if cfg.IF_IN_RPI:
    from hcsr04sensor import sensor


class DistanceSensor:
    def __init__(self, echo_pin, trig_pin):
        """
            Should be carefull while initialising LEDs. No checks here.
        """
        print(f"Distance Sensor pin configuring: {echo_pin}, {trig_pin}.")
        self.echo_pin = echo_pin
        self.trig_pin = trig_pin

    def get_distance(self):
        print("Distance Sensor: measuring distance")
        value = sensor.Measurement(self.trig_pin,
                                   self.echo_pin)
        raw_distance = value.raw_distance()
        return value.distance_metric(raw_distance)
