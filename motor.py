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
STEP_PIN = 27
DIR_PIN = 29

# Set GPIO mode and setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Function to step the motor
def step_motor(steps, direction):
    # Set direction
    GPIO.output(DIR_PIN, direction)

    # Step the motor for the specified number of steps
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.0001)  # Adjust this delay as needed for your motor
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.0001)  # Adjust this delay as needed for your motor

# Main program
if __name__ == "__main__":
    try:
        # Rotate motor 200 steps clockwise
        step_motor(200, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second

        # Rotate motor 200 steps counterclockwise
        step_motor(200, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second

        # Stop motor
        GPIO.output(STEP_PIN, GPIO.LOW)
        GPIO.output(DIR_PIN, GPIO.LOW)

    except KeyboardInterrupt:
        # Clean up GPIO on Ctrl+C
        GPIO.cleanup()


#Code source: https://www.youtube.com/watch?v=LUbhPKBL_IU
