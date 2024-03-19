from frames.test_selection_frame import TestSelectionFrame
from frames.strain_input_type_frame import StrainInputTypeFrame
from frames.constant_strain_input_frame import ConstantStrainTestInput
from frames.randomized_strain_input_frame import RandomizedStrainTestInput
from frames.wave_strain_input_frame import WaveStrainTestInput
from frames.settings_frame import Settings
from frames.test_output_frame import TestOutput
from frames.loadcell_calibration_frame import Calibration
from frames.home_frame import HomeFrame


import wx
import threading
import time

#import RPi.GPIO as GPIO
#from hx711 import HX711  # import the class HX711
from time import sleep
import motor_config

#--------------------------------------------------------------------------BACK-END CONTROLS---------------------------------------------
# This is where the majority of the back-end functionality will reside. Includes functions that control screen navigation, motor control
# load cell readings, running tests, exporting data, randomizing values, motor and load cell initializations, etc.

# Define Directions
global CW
global CCW
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise

motor_dict = motor_config.motor_dict                    #Pass by reference
#loadcell_dict = loadcell_config.loadcell_dict          #Pass by reference



def start_program():
    global home_frame
    home_frame = HomeFrame(None, -1, "BioReactor")
    #back_end.initialization() #initialize motors and load cells
    home_frame.Show()

def get_current_frame(frame_name):                       #determines which frame user is currently in, assign to existing global frame name class
    global current_frame
    match frame_name:
        case 'TestSelectionFrame':
            current_frame = test_selection_frame
        case 'StrainInputTypeFrame':
            current_frame = strain_input_type_frame
        case 'ConstantStrainTestInput':
            current_frame = constant_strain_test_frame
        case 'RandomizedStrainTestInput':
            current_frame = randomized_strain_test_frame
        case 'WaveStrainTestInput':
            current_frame = square_wave_strain_test_frame
        case 'Settings':
            current_frame = settings_frame
        case 'Calibration':
            current_frame = loadcell_calibration_frame
        case 'TestOutput':
            current_frame = live_test_frame


#TODO: Add functions for grabing max,min,and rate from each of the different strain type input tests


def on_motor_click(event):
    identity = event.GetEventObject().GetLabel()    #Returns which capsule selected
    global test_selection_frame
    test_selection_frame = TestSelectionFrame(identity)
    test_selection_frame.Show()

def on_compression_test_click(event, motor_name):
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()

def on_tensile_test_click(event, motor_name):
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()

def on_constant_test_click(event, motor_name, test_type):       #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global constant_strain_test_frame
    constant_strain_test_frame = ConstantStrainTestInput(motor_name, test_type, strain_type)
    constant_strain_test_frame.Show()

def on_random_test_click(event, motor_name, test_type):         #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global randomized_strain_test_frame
    randomized_strain_test_frame = RandomizedStrainTestInput(motor_name, test_type, strain_type)
    randomized_strain_test_frame.Show()

def on_square_wave_test_click(event, motor_name, test_type):    #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global square_wave_strain_test_frame
    square_wave_strain_test_frame = WaveStrainTestInput(motor_name, test_type, strain_type)
    square_wave_strain_test_frame.Show()

def on_settings_click(event, frame_name):
    get_current_frame(frame_name)
    current_frame.Destroy()
    global settings_frame
    settings_frame = Settings()
    settings_frame.Show()

def on_calibration_click(event):
    identity = event.GetEventObject().GetLabel()
    settings_frame.Destroy()
    global loadcell_calibration_frame
    loadcell_calibration_frame = Calibration(identity)
    loadcell_calibration_frame.Show()

def on_start_test_click(event, motor_name, test_type, strain_type):                  #TODO: WILL NEED TO ADD ANOTHER PARAMETER FOR THE STRAIN VALUES 
    identity = event.GetEventObject().GetLabel()
    constant_strain_test_frame.Destroy()
    global live_test_frame
    live_test_frame = TestOutput(motor_name, test_type, strain_type)
    live_test_frame.Show()
    
    home_frame.is_running(motor_name[-1])       #disable button, change color of button to red
    #thread = threading.Thread(target = run_motor_constant, args=(motor_name[-1], test_type, 1, 1,))
    thread = threading.Thread(target = thread_test, args=(motor_name,))
    thread.start()

def on_home_click(event, frame_name):
    get_current_frame(frame_name)
    current_frame.Destroy()
    

def thread_test(motor_name):
    for i in range(10):
        print(f"{motor_name} running: {i}")
        time.sleep(1)
    
    wx.CallAfter(home_frame.done_running, motor_name[-1])   #re-enabled button, change color back to default
    

#    gui_be.randomized_strain(10,100)


#function to initialize both motors and their respective load cells
""" def initialization():
	
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

	print("-------LOAD CELLS ARE READY-------") """

# function to run a motor depending on type of test (compression/tensile) - used for constant and randomized strain
""" def run_motor_constant(motor_name, test_name, strain_value, time_duration):		#TODO: have a way to convert strain value (in newtons) to step size equivalent to control motors
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
		#read_data(motor_name)	-----------------------------------------------> WILL NEED TO UNCOMMENT """
	









