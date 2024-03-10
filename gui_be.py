import RPi.GPIO as GPIO
from time import sleep
import motor_config
import loadcell_config
import random

#TODO: Convert data into .CSV file
#TODO: MAYBE COMBINE TWO INITIALIZATION METHODS (MOTOR AND LOADCELL) INTO 1, SO THAT THEY ARE BOTH CONNECTED!!!!!!

# Define Directions
global CW
global CCW
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise


motor_config.initialize_motors() 		#initialize motors
motor_dict = motor_config.motor_dict


def randomized_strain(min, max):		#function to select random strain value between lowest and highest
	return(random.randrange(min, max))


# function to run a motor depending on type of test (compression/tensile) - used for constant and randomized strain
def run_motor_constant(motor_name, test_name, strain_value, time_duration):		#TODO: have a way to convert strain value (in newtons) to step size equivalent to control motors
	if test_name=='Compression Test':											#TODO: have a way to convert time duration to something equivalent to control or sleep motors 
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

# function to run a motor depending on type of test (compression/tensile) - used for square wave input
def run_motor_wave(motor_name, test_name, min, max, time_duration):				#TODO: have a way to periodically control motor from low to high, high to low (square wave)
	pass

# Once finished clean everything up
#except KeyboardInterrupt:
#	GPIO.cleanup()

#Code source: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d



#TODO: Code for controlling loadcells

def test():
    for motor in a:
    	print(a[motor]['dir_pin'])

def status(name):
    print(name)