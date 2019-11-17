
import numpy as np

# Global config

# RPi
IF_IN_RPI = False  # False - will supress using RPI only libraries

HOST_IP = "192.168.1.76"
HOST_PORT = 65000


# Window
WINDOW_ORIGINAL_IMAGE = "Lab 4: Original"
WINDOW_MODIFIED_IMAGE = "Lab 4: Modified"

# Program
WAIT_KEY = "q"
WAIT_KEY_TIME = 10

# Stream
LOAD_STREAM = True
STREAM_RTSP_IP = "rtsp://192.168.1.68/554"  # Change ip and port
STREAM_WEB_ID = 0                           # Web camera

# LED
LED_PIN = 23

# Servo
SERVO_PIN = 25
SERVO_FREQUENCY = 50                        # Гц

# Filters
# Gray Threshold
THRESHOLD_VALUE = 50
THRESHOLD_MAXVALUE = 255

# Threshold of blue in HSV space
THRESHOLD_LOWER_BLUE = np.array([210, 25, 25])
THRESHOLD_UPPER_BLUE = np.array([280, 90, 90])

# Filter
FILTER_DIAMETER = 5
FILTER_SIGMA_COLOR = 175
FILTER_SIGMA_SPACE = 175

# Canny
CANNY_THRESHOLD_FIRST = 75
CANNY_THRESHOLD_SECOND = 200

# Contour/Center drawer
DRAW_CONTOUR = -1              # Draw all
DRAW_COLOR_BLUE = (255, 0, 0)  # Color: B G R
DRAW_COLOR_RED = (0, 0, 255)   # Color: B G R
DRAW_COLOR_GREEN = (0, 255, 0)   # Color: B G R
DRAW_THICKNESS = 3
DRAW_RADIUS = 7
DRAW_CENTER_RADIUS = 2
DRAW_CIRCLE_THICKNESS = -1

# Contour Selection Magic
AREA_APROXIMATION = 8
AREA_UPPER_BOUND = 50000
AREA_LOWER_BOUND = 1000
