import RPi.GPIO as GPIO
from time import sleep

# number of steps per revolution = 360/motor's step angle, which 
# for the haydon motor, the step angle is 1.8 from the data sheet
# therefore the number of steps required to complete one revolution is:
# 360/1.8 = 200


# Define GPIO pins
# Motor 1 GPIO setup
STEP_PIN_S1 = 33
DIR_PIN_S1 = 35

# Define Directions
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise

GPIO.setwarnings(False)

# Set GPIO mode and setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN_S1, GPIO.OUT)
GPIO.setup(DIR_PIN_S1, GPIO.OUT)
GPIO.output(DIR_PIN_S1, CW)

for x in range(500):		#turn in the CW direction
	GPIO.output(STEP_PIN_S1, GPIO.HIGH)
	sleep(0.005)
	GPIO.output(STEP_PIN_S1, GPIO.LOW)
	sleep(0.005)

sleep(1.0)

GPIO.output(DIR_PIN_S1, CCW) #turn in the CCW direction

for x in range(10000):
	GPIO.output(STEP_PIN_S1, GPIO.HIGH)
	sleep(0.005)
	GPIO.output(STEP_PIN_S1, GPIO.LOW)
	sleep(0.005)

# Once finished clean everything up
#except KeyboardInterrupt:
#	GPIO.cleanup()

#Code source: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d