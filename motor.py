# from time import sleep
# import RPi.GPIO as GPIO


# #Config for stepper motor 1
# DIR_PIN_S1 = 29        # Direction GPIO Pin motor 1
# STEP_PIN_S1 = 27       # Step GPIO Pin motor 1 
# CW = 1          # Clockwise 
# CCW = 0         # CounterClockwise
# SPR = 202       # Steps per Revolution (365 / 1.8)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR_PIN_S1, GPIO.OUT)
# GPIO.setup(STEP_PIN_S1, GPIO.OUT)
# GPIO.output(DIR_PIN_S1, CW)    #set initial rotation to cw

# step_count = SPR    #rotation
# delay = 0.005       # 1 sec / 202

# for i in range(step_count):
#     GPIO.output(STEP_PIN_S1, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP_PIN_S1, GPIO.LOW)
#     sleep(delay)

# sleep(0.5)
# GPIO.output(DIR_PIN_S1, CCW)   #set rotation to ccw
# for i in range(step_count):
#     GPIO.output(STEP_PIN_S1, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP_PIN_S1, GPIO.LOW)
#     sleep(delay)

import RPi.GPIO as GPIO
import time

# Define GPIO pins
STEP_PIN = 29
DIR_PIN = 31

# Define Directions
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise

# Set GPIO mode and setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
try:
	# Run forever.
	while True:
		GPIO.output(STEP_PIN, HIGH)
		GPIO.output(DIR_PIN, CW)
		sleep(5)
		GPIO.output(STEP_PIN, LOW)
		sleep(1)
		GPIO.output(STEP_PIN, HIGH)
		GPIO.output(DIR_PIN, CCW)	
		sleep(5)

# Once finished clean everything up
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()

#Code source: https://www.youtube.com/watch?v=LUbhPKBL_IU
