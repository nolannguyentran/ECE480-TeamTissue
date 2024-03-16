import RPi.GPIO as GPIO
from hx711 import HX711  # import the class HX711
from time import sleep
import motor_config
import loadcell_config
import random

#TODO: Convert data into .CSV file
#TODO: HAVE A WAY TO NOT DESTROY A FRAME WHEN THE MOTOR IS RUNNING, BUT HIDE IT, HAVE A BOOLEAN PARAMETER THAT CHECKS WHETHER THE MOTOR IS STILL RUNNING
#TODO: CREATE FUNCTION TO CALIBRATE LOADCELLS

# Define Directions
global CW
global CCW
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise


#motor_config.initialize_motors() 		#initialize motors
#loadcell_config.initialize_loadcells()
motor_dict = motor_config.motor_dict
loadcell_dict = loadcell_config.loadcell_dict


#function to initialize both motors and their respective load cells
def initialization():
	
	GPIO.setwarnings(False)

	# Set GPIO mode and setup pins for motors 1-4
	GPIO.setmode(GPIO.BOARD)
	for motor in motor_dict:
		GPIO.setup(motor_dict[motor]['step_pin'], GPIO.OUT, initial = GPIO.LOW)
	
	for motor in motor_dict:
		GPIO.setup(motor_dict[motor]['dir_pin'], GPIO.OUT, initial = GPIO.LOW)
	
	print("-------MOTORS ARE READY-------")
	
	global loadcell_A
	global loadcell_B
	global loadcell_C
	global loadcell_D

	# Create and set up all four load cells objects
	loadcell_A = HX711(dout_pin=loadcell_dict['A']['dout_pin'], pd_sck_pin=loadcell_dict['A']['pd_sck_pin'], channel=loadcell_dict['A']['channel'], gain=loadcell_dict['A']['gain']) 
	loadcell_B = HX711(dout_pin=loadcell_dict['B']['dout_pin'], pd_sck_pin=loadcell_dict['B']['pd_sck_pin'], channel=loadcell_dict['B']['channel'], gain=loadcell_dict['B']['gain']) 
	loadcell_C = HX711(dout_pin=loadcell_dict['C']['dout_pin'], pd_sck_pin=loadcell_dict['C']['pd_sck_pin'], channel=loadcell_dict['C']['channel'], gain=loadcell_dict['C']['gain']) 
	loadcell_D = HX711(dout_pin=loadcell_dict['D']['dout_pin'], pd_sck_pin=loadcell_dict['D']['pd_sck_pin'], channel=loadcell_dict['D']['channel'], gain=loadcell_dict['D']['gain']) 

	print("-------LOAD CELLS ARE READY-------")

def calibrate_loadcells():
	print("-------LOAD CELLS HAVE BEEN SUCCESSFULLY CALIBRATED!-------")
	

def read_data(motor_name):		#TODO: MUCH MORE WILL BE ADDED
    match motor_name:
        case 'A':
            loadcell_A.get_raw_data(loadcell_dict[motor_name]['num_readings'])
        case 'B':
            loadcell_B.get_raw_data(loadcell_dict[motor_name]['num_readings'])
        case 'C':
            loadcell_C.get_raw_data(loadcell_dict[motor_name]['num_readings'])
        case 'D':
            loadcell_D.get_raw_data(loadcell_dict[motor_name]['num_readings'])



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
		#read_data(motor_name)	---------------------------------------------> WILL NEED TO UNCOMMENT
	
	sleep(1.0)
	GPIO.output(motor_dict[motor_name]['dir_pin'], returning_rotation)

	for step in range(10000):
		GPIO.output(motor_dict[motor_name]['step_pin'], GPIO.HIGH)
		sleep(0.005)
		GPIO.output(motor_dict[motor_name]['step_pin'], GPIO.LOW)
		sleep(0.005)
		#read_data(motor_name)	-----------------------------------------------> WILL NEED TO UNCOMMENT

# function to run a motor depending on type of test (compression/tensile) - used for square wave input
def run_motor_wave(motor_name, test_name, min, max, time_duration):				#TODO: have a way to periodically control motor from low to high, high to low (square wave)
	pass

# Once finished clean everything up
#except KeyboardInterrupt:
#	GPIO.cleanup()





#Code source: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d
#code source: https://pypi.org/project/hx711/ 
#code source: https://github.com/mpibpc-mroose/hx711/blob/master/example.py 

