from frames.test_selection_frame import TestSelectionFrame
from frames.strain_input_type_frame import StrainInputTypeFrame
from frames.constant_strain_input_frame import ConstantStrainTestInput
from frames.randomized_strain_input_frame import RandomizedStrainTestInput
from frames.wave_strain_input_frame import WaveStrainTestInput
from frames.settings_frame import Settings
from frames.jobs_frame import Jobs
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


motor_a_flag = threading.Event()  # flags used to stop threads
motor_b_flag = threading.Event()
motor_c_flag = threading.Event()
motor_d_flag = threading.Event()


# Define Directions
global CW
global CCW
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise

motor_dict = motor_config.motor_dict                    #Pass by reference
#loadcell_dict = loadcell_config.loadcell_dict          #Pass by reference

#TODO: MAYBE ADD GLOBAL LIST FOR EACH MOTORS ('A', 'B', 'C', 'D') TO LATER BE CONVERTED INTO .CSV FILE

def start_program():
    global home_frame
    home_frame = HomeFrame(None, -1, "BioReactor")
    #back_end.initialization() #initialize motors and load cells
    home_frame.Show()
    global jobs_frame
    jobs_frame = Jobs()
    

def get_current_frame(frame_name):                       #determines which frame user is currently in, assign to existing global frame name class
    global current_frame                                 #TODO: NEED A CHECK IF THE USER IS CURRENTLY ON THE HOME PAGE, IF THEY ARE, DON'T DESTROY THE FRAME, I.E. PRESSING THE SETTINGS, JOBS BUTTON WHEN THE USER IS IN THE HOME DASHBOARD
    match frame_name:                                    #<---------------------------------might need to add settings and job frame
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
        case 'Jobs':                                                   #TODO: BIG PROBLEM , DONT DESTROY JOB, BUT HIDE IT
            current_frame = jobs_frame
        case 'HomeFrame':
            current_frame = home_frame


#TODO: Add functions for grabing max,min,and rate from each of the different strain type input tests


def on_motor_click(event):                          #TODO: ADDED IF STATEMENT DETERMINING WHETHER THE MOTOR IS CURRENTLY RUNNING AND NAVIGATE USER TO THE APPROPIATE PAGE
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

def on_jobs_click(event, frame_name):
    get_current_frame(frame_name)
    if current_frame != home_frame:
        current_frame.Destroy()
    
    jobs_frame.Show()


def on_calibration_click(event):
    identity = event.GetEventObject().GetLabel()
    settings_frame.Destroy()
    global loadcell_calibration_frame
    loadcell_calibration_frame = Calibration(identity)
    loadcell_calibration_frame.Show()




def on_start_test_click(event, motor_name, test_type, strain_type):                  #TODO: WILL NEED TO ADD ANOTHER PARAMETER FOR THE STRAIN VALUES 
    identity = event.GetEventObject().GetLabel()
    constant_strain_test_frame.Destroy()
    #global live_test_frame
    #live_test_frame = TestOutput(motor_name, test_type, strain_type)
    #live_test_frame.Show()
    
    jobs_frame.Show()
    
    home_frame.is_running(motor_name)       #disable button, change color of button to red
    jobs_frame.is_running(motor_name, test_type, strain_type)
    #thread = threading.Thread(target = run_motor_constant, args=(motor_name[-1], test_type, 1, 1,))
    global thread_a
    global thread_b
    global thread_c
    global thread_d
    
    thread_a = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_a_flag))
    thread_b = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_b_flag))
    thread_c = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_c_flag))
    thread_d = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_d_flag))
    match motor_name[-1]:
            case 'A':
                thread_a.start()
            case 'B':
                thread_b.start()
            case 'C':
                thread_c.start()
            case 'D':
                thread_d.start()
    #thread = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type,))
    #thread.start()

def on_home_click(event, frame_name):
    get_current_frame(frame_name)
    if current_frame == jobs_frame:
        current_frame.Hide()
    else:
        current_frame.Destroy()
    

def thread_test(motor_name, test_type, strain_type, stop_flag):
    for i in range(10):
        if stop_flag.is_set():
            break
        print(f"{motor_name} running: {i}")
        time.sleep(1)
    
    wx.CallAfter(jobs_frame.done_running, motor_name, test_type, strain_type)
    

def on_task_click(event, motor_name, test_type, strain_type):           #function for buttons in jobs page after a test is finished
    identity = event.GetEventObject().GetLabel()
    jobs_frame.Hide()
    global live_test_frame
    live_test_frame = TestOutput(motor_name, test_type, strain_type)
    live_test_frame.Show()


def on_stop_test_click(event):              #function for 'Stop Test' buttons in 'Jobs' page
    motor_name = event.GetEventObject().myname                                    #TODO: call function to stop specific thread, and maybe function to reset linear actuator position back to original 'starting' position (in cm?)
    match motor_name:
            case 'A':
                motor_a_flag.set()
            case 'B':
               motor_b_flag.set()
            case 'C':
                motor_c_flag.set()
            case 'D':
                motor_d_flag.set()

def clear_test_results(event, motor_name, frame_name):
    home_frame.done_running(motor_name)
    jobs_frame.clear_test(motor_name)
    get_current_frame(frame_name)
    current_frame.Destroy()
    jobs_frame.Show()
    match motor_name[-1]:
            case 'A':
                motor_a_flag.clear()
            case 'B':
               motor_b_flag.clear()
            case 'C':
                motor_c_flag.clear()
            case 'D':
                motor_d_flag.clear()


def export_test_results(event, motor_name):
    pass                        #TODO: call function to export list to .CSV file

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
	









