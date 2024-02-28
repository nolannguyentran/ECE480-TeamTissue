import RPi.GPIO as GPIO
from time import sleep
#Import variables from loadcell.py for PID control
#from loadcell import LOADCELLOUTPUT1, LOADCELLOUTPUT2, LOADCELLOUTPUT3, LOADCELLOUTPUT4

# number of steps per revolution = 360/motor's step angle, which 
# for the haydon motor, the step angle is 1.8 from the data sheet
# therefore the number of steps required to complete one revolution is:
# 360/1.8 = 200


# Define GPIO pins
# Motor 1 GPIO setup
#STEP_PIN_S1 = 33
#DIR_PIN_S1 = 35
# Motor 2 GPIO setup -- ##CHANGE GPIO DEPENDING ON CURRENT WIRING##
# STEP_PIN_S2 = 
# DIR_PIN_S2 = 
# # Motor 3 GPIO setup
# STEP_PIN_S3 = 
# DIR_PIN_S3 = 
# # Motor 4 GPIO setup
# STEP_PIN_S4 = 
# DIR_PIN_S4 = 

#List of all Motor channels to be set - add as implemented to the list
#STEP_CHANNELS = [STEP_PIN_S1]	#, STEP_PIN_S2, STEP_PIN_S3, STEP_PIN_S4]
#DIR_CHANNELS = [DIR_PIN_S1]		#, STEP_PIN_S2, STEP_PIN_S3, STEP_PIN_S4]

# Define Directions

motor_dict = {					#dictionary containing respective step/dir pin for each motor configuration
	'A':{
		'step_pin':33,
		'dir_pin': 35
	},
	'B':{
		'step_pin':1,
		'dir_pin': 2
	},
	'C':{
		'step_pin':3,
		'dir_pin': 4
	},
	'D':{
		'step_pin':5,
		'dir_pin': 6
	},
}

def initialize_motors():
	CW = 1          # Clockwise 
	CCW = 0         # CounterClockwise

	starting_rotation = CW
	returning_rotation = CCW

	GPIO.setwarnings(False)

	# Set GPIO mode and setup pins for motors 1-4
	GPIO.setmode(GPIO.BOARD)
	for motor in motor_dict:
		 GPIO.setup(motor_dict[motor]['step_pin'], GPIO.OUT, initial = GPIO.LOW)
		#GPIO.setup(STEP_CHANNELS, GPIO.OUT, initial = GPIO.LOW)
	for motor in motor_dict:
    	 GPIO.setup(motor_dict[motor]['dir_pin'], GPIO.OUT, initial = GPIO.LOW)
		#GPIO.setup(DIR_CHANNELS, GPIO.OUT, initial = GPIO.LOW)

def run_motor(motor_name, test_name):
	if test_name=='Compression Test':
		starting_rotation = CW
		returning_rotation = CCW
		
	else:
		starting_rotation = CCW
		returning_rotation = CW
		
	GPIO.output(motor_dict[motor_name]['dir_pin'], starting_rotation)

	for step in range(500):
		 GPIO.output(motor_dict[motor_name]['step_pin'], GPIO.HIGH)
		 sleep(0.005)
		 GPIO.output(motor_dict[motor_name]['step_pin'], GPIO.LOW)
		 sleep(0.005)
	
	sleep(1.0)
	GPIO.output(motor_dict[motor_name]['dir_pin'], returning_rotation)

	for step in range(10000):
		 GPIO.output(motor_dict[motor_name]['step_pin'], GPIO.HIGH)
		 sleep(0.005)
		 GPIO.output(motor_dict[motor_name]['step_pin'], GPIO.LOW)
		 sleep(0.005)

# Once finished clean everything up
#except KeyboardInterrupt:
#	GPIO.cleanup()

#Code source: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d