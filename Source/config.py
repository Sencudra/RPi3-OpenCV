
import logging
import numpy as np


"""
    Common
"""

# Logger
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

# Global
IF_IN_RPI = True  # defaul: False - will NOT use RPi libraries.

# Text
DEFAULT_ENCODING = 'utf8'

# Network
LOCAL_HOST_IP = "127.0.0.1"
HOST_IP = "192.168.1.135"
HOST_PORT = 65201
SOCKET_TIMEOUT = 1

# Stream
LOAD_STREAM = False                         # Default: False - wil NOT use rtsp
STREAM_RTSP_IP = "rtsp://192.168.1.68/554"  # Change ip and port
STREAM_WEB_ID = 0                           # Default: 1 - Embedded webcam

# Window
WINDOW_ORIGINAL_IMAGE = "Lab 4: Original"
WINDOW_MODIFIED_IMAGE = "Lab 4: Modified"

# Program
WAIT_KEY = "q"
WAIT_KEY_TIME = 1


"""
    Peripherals
"""

# LED
LED_PIN = 14

# Servo
SERVO_PIN = 15
SERVO_FREQUENCY = 50

# Buzzer
BUZZER_PIN = 18
BUZZER_DEFAULT_FREQUENCY = 300
BUZZER_DEFAULT_LOUDNESS = 0

# Distance sensor
DISTANCE_SENSOR_ECHO_PIN = 23
DISTANCE_SENSOR_TRIG_PIN = 24
DUSTANCE_SENSOR_MAX = 200

"""
    Filters
"""
# Gray Threshold
THRESHOLD_VALUE = 10
THRESHOLD_MAXVALUE = 255

# Threshold of blue in HSV space
THRESHOLD_LOWER_BLUE = np.array([210, 15, 15])
THRESHOLD_UPPER_BLUE = np.array([280, 90, 90])

# Filter
FILTER_DIAMETER = 2
FILTER_SIGMA_COLOR = 175
FILTER_SIGMA_SPACE = 175

# Canny
CANNY_THRESHOLD_FIRST = 75
CANNY_THRESHOLD_SECOND = 200

# Contour/Center drawer
DRAW_CONTOUR = -1               # Draw all
DRAW_COLOR_BLUE = (255, 0, 0)   # Color: B G R
DRAW_COLOR_RED = (0, 0, 255)    # Color: B G R
DRAW_COLOR_GREEN = (0, 255, 0)  # Color: B G R
DRAW_THICKNESS = 3
DRAW_RADIUS = 7
DRAW_CENTER_RADIUS = 2
DRAW_CIRCLE_THICKNESS = -1

# Contour Selection Magic
AREA_APROXIMATION = 8
AREA_UPPER_BOUND = 50000
AREA_LOWER_BOUND = 1000
