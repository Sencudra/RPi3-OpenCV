
import random
import logging as log

import config as cfg

if cfg.IF_IN_RPI:
    from hcsr04sensor import sensor


class DistanceSensor:
    def __init__(self, echo_pin, trig_pin):
        """
            Should be carefull while initialising LEDs. No checks here.
        """
        log.info(f"DS - Initialising. Pins used: {echo_pin}, {trig_pin}.")
        self.echo_pin = echo_pin
        self.trig_pin = trig_pin

    def get_distance(self):
        log.info("DS - Measuring distance...")

        distance = None

        if cfg.IF_IN_RPI:
            value = sensor.Measurement(self.trig_pin,
                                       self.echo_pin)
            raw_distance = value.raw_distance()
            distance = value.distance(raw_distance)
        else:
            distance = random.randint(0, 500)

        log.info(f"DS - Distance: {distance} cm measured")
        return distance
