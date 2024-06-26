from frames.test_selection_frame import TestSelectionFrame
from frames.strain_input_type_frame import StrainInputTypeFrame
from frames.constant_strain_input_frame import ConstantStrainTestInput
from frames.wave_strain_input_frame import WaveStrainTestInput
from frames.settings_frame import Settings
from frames.jobs_frame import Jobs
from frames.test_output_frame import TestOutput
from frames.loadcell_selection_calibration_frame import LoadcellSelectionCalibration
from frames.attach_known_weight_frame import AttachWeightFrame
from frames.loadcell_calibration_frame import Calibration
from frames.loadcell_calibration_success_frame import CalibrationSuccess
from frames.data_plot_frame import DataPlotFrame
from frames.home_frame import HomeFrame


import wx
import threading
import time
import csv
import matplotlib.pyplot as plt
from datetime import datetime

import RPi.GPIO as GPIO
from hx711 import HX711  # import the class HX711

import motor_config
import loadcell_config
from time import sleep

#--------------------------------------------------------------------------BACK-END CONTROLS---------------------------------------------
# This is where the majority of the back-end functionality will reside. Includes functions that control screen navigation, motor control
# load cell readings, running tests, exporting data, motor and load cell initializations, etc.


#TODO: IN DOCUMENTATION MENTION THAT ALL MOTORS MUST BE STOPPED BEFORE CLICKING ON THE 'X' IN HOMESCREEN, UNLESS IMPLEMENT AN EMERGENCY SHUTOFF?

motor_a_flag = threading.Event()  # flags used to stop motor threads
motor_b_flag = threading.Event()
motor_c_flag = threading.Event()
motor_d_flag = threading.Event()

motor_a_lc_flag = threading.Event()
motor_b_lc_flag = threading.Event()
motor_c_lc_flag = threading.Event()
motor_d_lc_flag = threading.Event() # flag used to stop load cell threads

# Define Directions
global CW
global CCW
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise

motor_dict = motor_config.motor_dict                    #Pass by reference
loadcell_dict = loadcell_config.loadcell_dict          #Pass by reference

csv_constant_strain_fields = ['Time', 'Strain Value (grams)']  #csv headers for constrant strain tests
csv_square_wave_strain_fields = ['Time', 'Strain Value (grams)']   #csv headers for square wave strain tests
capsule_a_list = [] #list holding loadcell data
capsule_b_list = []
capsule_c_list = []
capsule_d_list = []

def start_program():
    global home_frame
    home_frame = HomeFrame()
    initialization() #initialize motors and load cells
    home_frame.Show()
    global jobs_frame
    jobs_frame = Jobs()
    
def get_current_frame(frame_name):                       #function that determines which frame user is currently in, assign to existing global frame name class
    global current_frame                                 
    match frame_name:                                    
        case 'TestSelectionFrame':
            current_frame = test_selection_frame
        case 'StrainInputTypeFrame':
            current_frame = strain_input_type_frame
        case 'ConstantStrainTestInput':
            current_frame = constant_strain_test_frame
        case 'WaveStrainTestInput':
            current_frame = square_wave_strain_test_frame
        case 'Settings':
            current_frame = settings_frame
        case 'LoadcellSelectionCalibration':
            current_frame = loadcell_selection_calibration_frame
        case 'AttachWeightFrame':
            current_frame = attach_known_weight_frame
        case 'Calibration':
            current_frame = loadcell_calibration_frame
        case 'CalibrationSuccess':
            current_frame = loadcell_calibration_success_frame
        case 'TestOutput':
            current_frame = live_test_frame
        case 'Jobs':                                                   
            current_frame = jobs_frame
        case 'HomeFrame':
            current_frame = home_frame
        case 'DataPlotFrame':
            current_frame = data_plot_frame

def plot_data(filename):     #function to plot a graph based on exported .CSV data
    # Lists to store time and strain .CSV data
    times = []
    strains = []
    # Open the CSV file
    with open(filename, 'r') as test_info:
        csv_reader = csv.reader(test_info)
        header = next(csv_reader)
        for row in csv_reader:
            # Split the row into time and strain
            time_str = row[0].split(',')
            strain_str = row[1].split(',')
        
            # Convert time string to datetime object
            for item in time_str:
                time_num = datetime.strptime(item, '%H:%M:%S:%f')
                # Append the datetime object to the times list
                times.append(time_num)
            
            # Convert strain string to integer
            for item in strain_str:
                if item=='False':
                    strain_int = 0
                else:
                    strain_int = int(float(item))
                # Append strain to list
                strains.append(strain_int)

    sorted_indices = sorted(range(len(times)), key=lambda i: times[i])
    times_sorted = [times[i] for i in sorted_indices]
    strains_sorted = [strains[i] for i in sorted_indices]

    figure, ax = plt.subplots(figsize=(4,3))
    # Plot time vs. strain
    ax.plot(times_sorted, strains_sorted)
    ax.set_xlabel('Time')
    ax.set_ylabel('Strain (grams)')
    ax.set_title('Strain vs. Time')
    #ax.set_xticklabels(ax.get_xticks(),rotation=45)
    ax.grid(True)
    test_info.close()
    return figure
    
def time_conversion(seconds):       #convert to format: H:M:S:milli
    minutes = seconds//60
    hours = minutes//60  #hour-th place
    seconds = seconds%60 #second-th place
    minutes = minutes%60 #minute-th place
    milliseconds = int((seconds%1)*100)  #millisecond-th place
    converted_time = '{0}:{1}:{2}:{3}'.format(int(hours), int(minutes), int(seconds), milliseconds)
    return converted_time

def step_conversion(displacement):      #convert linear displacement in millimeters to motor step count
    if int(displacement)>38.1 or int(displacement)<0:
        raise ValueError("Input exceeds 38.1 mm or is less than 0 mm!")
    else:
        return int(float(displacement)/0.003)

def on_motor_click(event):                          #function for each of the 'Capsule' buttons on the home screen
    identity = event.GetEventObject().GetLabel()    #Returns which capsule selected
    global test_selection_frame
    test_selection_frame = TestSelectionFrame(identity)
    test_selection_frame.Show()

def on_compression_test_click(event, motor_name):   #function for 'Compression Test' button in Test Selection screen
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()

def on_tensile_test_click(event, motor_name):       #function for 'Tensile Test' button in Test Selection screen
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

def on_square_wave_test_click(event, motor_name, test_type):    #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global square_wave_strain_test_frame
    square_wave_strain_test_frame = WaveStrainTestInput(motor_name, test_type, strain_type)
    square_wave_strain_test_frame.Show()

def on_settings_click(event, frame_name):           #function for 'Settings' button 
    if frame_name == 'DataPlotFrame':
        DataPlotFrame.on_close()
        data_plot_frame.Destroy()
    get_current_frame(frame_name)
    if current_frame != home_frame:
        current_frame.Destroy()
    global settings_frame
    settings_frame = Settings()
    settings_frame.Show()

def on_jobs_click(event, frame_name):               #function for 'Jobs' button
    if frame_name == 'DataPlotFrame':
        DataPlotFrame.on_close()
        data_plot_frame.Destroy()
    get_current_frame(frame_name)
    if current_frame != home_frame:
        current_frame.Destroy()
    jobs_frame.Show()

def on_calibration_click(event, frame_name):        #function for "Calibration" button in Settings Page
    identity = event.GetEventObject().GetLabel()
    get_current_frame(frame_name)
    current_frame.Destroy()
    global loadcell_selection_calibration_frame
    loadcell_selection_calibration_frame = LoadcellSelectionCalibration(identity)
    loadcell_selection_calibration_frame.Show()
   
def on_loadcell_click(event, frame_name):       #function for the four load cell calibration selection 
    identity = event.GetEventObject().GetLabel()
    get_current_frame(frame_name)
    current_frame.Destroy()
    match identity[-1]:
        case 'A':
            error = loadcell_A.zero()
            if error:
                raise ValueError("Tare was unsuccessful")
            print("load cell A is tared!")
            raw_loadcell_reading = loadcell_A.get_raw_data_mean()
        case 'B':
            error = loadcell_B.zero()
            if error:
                raise ValueError("Tare was unsuccessful")
            print("load cell B is tared!")
            raw_loadcell_reading = loadcell_B.get_raw_data_mean()
        case 'C':
            error = loadcell_C.zero()
            if error:
                raise ValueError("Tare was unsuccessful")
            print("load cell C is tared!")
            raw_loadcell_reading = loadcell_C.get_raw_data_mean()
        case 'D':
            error = loadcell_D.zero()
            if error:
                raise ValueError("Tare was unsuccessful")
            print("load cell D is tared!")
            raw_loadcell_reading = loadcell_D.get_raw_data_mean()
            
    if raw_loadcell_reading:
        print("Data subtracted by offset but still not converted to units: ", raw_loadcell_reading)
    else:
        print('invalid data', raw_loadcell_reading)
    
    global attach_known_weight_frame
    attach_known_weight_frame = AttachWeightFrame(identity)
    attach_known_weight_frame.Show()

def on_next_click(event, frame_name, loadcell_name):        #function for next button after attaching known weight to loadcell to calibrate
    get_current_frame(frame_name)
    current_frame.Destroy()
    global loadcell_calibration_frame
    loadcell_calibration_frame = Calibration(loadcell_name)
    loadcell_calibration_frame.Show()

def on_enter_known_weight_click(event, frame_name, loadcell_name, known_weight_value):
    get_current_frame(frame_name)
    current_frame.Destroy()
    try:
            known_weight_grams = float(known_weight_value)
            print("Known weight in grams: ",known_weight_grams)
    except ValueError:
            print('Expected integer or float but I recieved: ', known_weight_value)

    match loadcell_name[-1]:
        case 'A':
            #print("load cell A is tared!")
            loadcell_reading = loadcell_A.get_data_mean()
            if loadcell_reading:
                print('Mean value from load cell A is subtracted by offset:', loadcell_reading)
        
                ratio = loadcell_reading/known_weight_grams
                loadcell_A.set_scale_ratio(ratio)
                print("Ratio is set!")
            else:
                raise ValueError('Value cannot be read')
            
        case 'B':
           #print("load cell B is tared!")
           loadcell_reading = loadcell_B.get_data_mean()
           if loadcell_reading:
                print('Mean value from load cell B is subtracted by offset:', loadcell_reading)
        
                ratio = loadcell_reading/known_weight_grams
                loadcell_B.set_scale_ratio(ratio)
                print("Ratio is set!")
           else:
                raise ValueError('Value cannot be read')
            
        case 'C':
            #print("load cell C is tared!")
            loadcell_reading = loadcell_C.get_data_mean()
            if loadcell_reading:
                print('Mean value from load cell C is subtracted by offset:', loadcell_reading)
        
                ratio = loadcell_reading/known_weight_grams
                loadcell_C.set_scale_ratio(ratio)
                print("Ratio is set!")
            else:
                raise ValueError('Value cannot be read')
            
        case 'D':
            #print("load cell D is tared!")
            loadcell_reading = loadcell_D.get_data_mean()
            if loadcell_reading:
                print('Mean value from load cell D is subtracted by offset:', loadcell_reading)
        
                ratio = loadcell_reading/known_weight_grams
                loadcell_D.set_scale_ratio(ratio)
                print("Ratio is set!")
            else:
                raise ValueError('Value cannot be read')
    
    print("The known weight value in grams is: "+known_weight_value)

    global loadcell_calibration_success_frame
    loadcell_calibration_success_frame = CalibrationSuccess(loadcell_name)
    loadcell_calibration_success_frame.Show()

def on_start_test_click(event, motor_name, test_type, strain_type, strain_input_1, strain_input_2, time_input, frame_name):                  #strain_input_1 is Minimum strain value for wave test or 0 for constant strain test
    identity = event.GetEventObject().GetLabel()                                                                                 #strain_input_2 is Maximum strain value for wave test or constant strain value for constant strain test
    get_current_frame(frame_name)
    current_frame.Destroy()
    jobs_frame.Show()
    
    home_frame.is_running(motor_name)       #disable button, change color of button to red
    jobs_frame.is_running(motor_name, test_type, strain_type)
    
    global thread_a
    global thread_b
    global thread_c
    global thread_d

    global thread_a_lc
    global thread_b_lc
    global thread_c_lc
    global thread_d_lc

    if strain_type=='Constant Strain':
        match motor_name[-1]:
            case 'A':
                """ thread_a = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_a_flag, strain_input_2, time_input)) """
                thread_a = threading.Thread(target = run_motor_constant, args=(motor_name, test_type, strain_type, strain_input_2, time_input, motor_a_flag))
                thread_a.start()
                thread_a_lc = threading.Thread(target = read_data, args=(motor_name, time_input))
            case 'B':
                """ thread_b = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_b_flag, strain_input_2, time_input)) """
                thread_b = threading.Thread(target = run_motor_constant, args=(motor_name, test_type, strain_type, strain_input_2, time_input, motor_b_flag))
                thread_b.start()
                thread_b_lc = threading.Thread(target = read_data, args=(motor_name, time_input))
            case 'C':
                """ thread_c = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_c_flag, strain_input_2, time_input)) """
                thread_c = threading.Thread(target = run_motor_constant, args=(motor_name, test_type, strain_type, strain_input_2, time_input, motor_c_flag))
                thread_c.start()
                thread_c_lc = threading.Thread(target = read_data, args=(motor_name, time_input))
            case 'D':
                """ thread_d = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_d_flag, strain_input_2, time_input)) """
                thread_d = threading.Thread(target = run_motor_constant, args=(motor_name, test_type, strain_type, strain_input_2, time_input, motor_d_flag))
                thread_d.start()
                thread_d_lc = threading.Thread(target = read_data, args=(motor_name, time_input))
    else:                                           #user chose square wave strain
        match motor_name[-1]:
            case 'A':
                """ thread_a = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_a_flag, strain_input_2, time_input)) """
                thread_a = threading.Thread(target = run_motor_wave, args=(motor_name, test_type, strain_type, strain_input_1, strain_input_2, time_input, motor_a_flag))
                thread_a.start()
                thread_a_lc = threading.Thread(target = read_data_wave, args=(motor_name, time_input))
                thread_a_lc.start()
            case 'B':
                """ thread_b = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_b_flag, strain_input_2, time_input)) """
                thread_b = threading.Thread(target = run_motor_wave, args=(motor_name, test_type, strain_type, strain_input_1, strain_input_2, time_input, motor_b_flag))
                thread_b.start()
                thread_b_lc = threading.Thread(target = read_data_wave, args=(motor_name, time_input))
                thread_b_lc.start()
            case 'C':
                """ thread_c = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_c_flag, strain_input_2, time_input)) """
                thread_c = threading.Thread(target = run_motor_wave, args=(motor_name, test_type, strain_type, strain_input_1, strain_input_2, time_input, motor_c_flag))
                thread_c.start()
                thread_c_lc = threading.Thread(target = read_data_wave, args=(motor_name, time_input))
                thread_c_lc.start()
            case 'D':
                """ thread_d = threading.Thread(target = thread_test, args=(motor_name, test_type, strain_type, motor_d_flag, strain_input_2, time_input)) """
                thread_d = threading.Thread(target = run_motor_wave, args=(motor_name, test_type, strain_type, strain_input_1, strain_input_2, time_input, motor_d_flag))
                thread_d.start()
                thread_d_lc = threading.Thread(target = read_data_wave, args=(motor_name, time_input))
                thread_d_lc.start()       
            
def on_home_click(event, frame_name):                   #function for 'Home' button
    if frame_name == 'DataPlotFrame':
        DataPlotFrame.on_close()
        data_plot_frame.Destroy()
    get_current_frame(frame_name)
    if current_frame == jobs_frame:
        current_frame.Hide()
    else:
        current_frame.Destroy()

def thread_test(motor_name, test_type, strain_type, stop_flag, strain_input, duration):     #function that simulate a test (only used when not connected to bioreactor)
    time_target = float(duration)
    start_time = time.time()
    #print(step_conversion(20))
    time_elapsed = 0
    while True:
        if stop_flag.is_set() or time_elapsed >= time_target:
            break
        end_time_increment = time.time()
        time_elapsed = end_time_increment - start_time
        print(f"{motor_name} running with strain: {step_conversion(strain_input)} grams...at time: {time_conversion(time_elapsed)}")
        capsule_b_list.append([time_conversion(time_elapsed), strain_input])
    
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
                motor_a_lc_flag.set()
            case 'B':
               motor_b_flag.set()
               motor_b_lc_flag.set()
            case 'C':
                motor_c_flag.set()
                motor_c_lc_flag.set()
            case 'D':
                motor_d_flag.set()
                motor_d_lc_flag.set()

def clear_test_results(event, motor_name, frame_name):      #function for 'Clear Test' after clicking on a completed task in the 'Jobs' page
    home_frame.done_running(motor_name)
    jobs_frame.clear_test(motor_name)
    get_current_frame(frame_name)
    current_frame.Destroy()
    jobs_frame.Show()
    match motor_name[-1]:
            case 'A':
                motor_a_flag.clear()
                motor_a_lc_flag.clear()
                capsule_a_list.clear()
            case 'B':
               motor_b_flag.clear()
               motor_b_lc_flag.clear()
               capsule_b_list.clear()
            case 'C':
                motor_c_flag.clear()
                motor_c_lc_flag.clear()
                capsule_c_list.clear()
            case 'D':
                motor_d_flag.clear()
                motor_d_lc_flag.clear()
                capsule_d_list.clear()
    

def remove_space(string):   #function to remove spaces in strings
    return string.replace(" ", "")

def export_test_results(event, motor_name, test_type, strain_type, frame_name):     #function that export test results to a .CSV file
    home_frame.done_running(motor_name)
    jobs_frame.clear_test(motor_name)
    get_current_frame(frame_name)
    current_frame.Destroy()

    filename = "/home/Tissue_Cap/Desktop/Capsule_{capsule}_{test}_{strain}.csv".format(capsule = motor_name[-1], test = remove_space(test_type), strain = remove_space(strain_type))
    """ filename = "Capsule_{capsule}_{test}_{strain}.csv".format(capsule = motor_name[-1], test = remove_space(test_type), strain = remove_space(strain_type)) """
    with open(filename, 'w', newline='') as f:
        file_writer = csv.writer(f)
        if strain_type=='Constant Strain':                                                              
            file_writer.writerow(csv_constant_strain_fields)
        else:                                                                  #user chose square wave...
            file_writer.writerow(csv_square_wave_strain_fields) 
        
        match motor_name[-1]:
            case 'A':
                file_writer.writerows(capsule_a_list)
                motor_a_flag.clear()
                motor_a_lc_flag.clear()
                capsule_a_list.clear()
            case 'B':
                file_writer.writerows(capsule_b_list)
                motor_b_flag.clear()
                motor_b_lc_flag.clear()
                capsule_b_list.clear()
            case 'C':
                file_writer.writerows(capsule_c_list)
                motor_c_flag.clear()
                motor_c_lc_flag.clear()
                capsule_c_list.clear()
            case 'D':
                file_writer.writerows(capsule_d_list)
                motor_d_flag.clear()
                motor_d_lc_flag.clear()
                capsule_d_list.clear()
    f.close()
    global data_plot_frame
    data_plot_frame = DataPlotFrame(motor_name, test_type, strain_type)
    data_plot_frame.Show()   

def exit_application(event):        #function for 'X' button on Homescreen
    jobs_frame.Destroy()
    home_frame.Destroy()

#function to initialize both motors and their respective load cells
def initialization():
    
    GPIO.setwarnings(False)

    # Set GPIO mode and setup pins for motors 1-4
    GPIO.setmode(GPIO.BOARD)

    for motor in motor_dict:
        GPIO.setup(motor_dict[motor]['enable_pin'], GPIO.OUT, initial = GPIO.LOW)
        print(f"[MOTOR {motor} ENABLE PIN SET UP SUCCESSFULLY]")

    for motor in motor_dict:
        GPIO.setup(motor_dict[motor]['step_pin'], GPIO.OUT, initial = GPIO.LOW)
        print(f"[MOTOR {motor} STEP PIN INIATED SUCCESSFULLY]")
    
    for motor in motor_dict:
        GPIO.setup(motor_dict[motor]['dir_pin'], GPIO.OUT, initial = GPIO.LOW)
        print(f"[MOTOR {motor} DIRECTION INIATED SUCCESSFULLY]")
    
    print("---------MOTORS ARE READY!--------")
    
    global loadcell_A
    global loadcell_B
    global loadcell_C
    global loadcell_D

    # Create and set up all four load cells objects
    loadcell_A = HX711(dout_pin=loadcell_dict['A']['dout_pin'], pd_sck_pin=loadcell_dict['A']['pd_sck_pin']) 
    print("[LOAD CELL A INIATED SUCCESSFULLY]")
    loadcell_B = HX711(dout_pin=loadcell_dict['B']['dout_pin'], pd_sck_pin=loadcell_dict['B']['pd_sck_pin']) 
    print("[LOAD CELL B INIATED SUCCESSFULLY]")
    loadcell_C = HX711(dout_pin=loadcell_dict['C']['dout_pin'], pd_sck_pin=loadcell_dict['C']['pd_sck_pin']) 
    print("[LOAD CELL C INIATED SUCCESSFULLY]")
    loadcell_D = HX711(dout_pin=loadcell_dict['D']['dout_pin'], pd_sck_pin=loadcell_dict['D']['pd_sck_pin']) 
    print("[LOAD CELL D INIATED SUCCESSFULLY]")

    print("-------LOAD CELLS ARE READY!-------")
    
def read_data_wave(motor_name, duration):
    print('Current weight on the scale in grams and force in Newtons is: ')
    time_target = float(duration)
    start_time = time.time()

    time_elapsed = 0
    match motor_name[-1]:
        case 'A':
            while True:
                if motor_a_lc_flag.is_set():
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_a = ((loadcell_A.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_A.get_weight_mean(1)} grams...{newton_mean_a}...at time: {time_conversion(time_elapsed)}")
                capsule_a_list.append([time_conversion(time_elapsed), loadcell_A.get_weight_mean(1)])
       
        case 'B':
            while True:
                if motor_b_lc_flag.is_set():
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_b = ((loadcell_B.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_B.get_weight_mean(1)} grams...{newton_mean_b} newtons...at time: {time_conversion(time_elapsed)}")
                capsule_b_list.append([time_conversion(time_elapsed), loadcell_B.get_weight_mean(1)])
        
        case 'C':
            while True:
                if motor_c_lc_flag.is_set():
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_c = ((loadcell_C.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_C.get_weight_mean(1)} grams...{newton_mean_c} newtons...at time: {time_conversion(time_elapsed)}")
                capsule_c_list.append([time_conversion(time_elapsed), loadcell_C.get_weight_mean(1)])
        
        case 'D':
            while True:
                if motor_d_lc_flag.is_set():
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_d = ((loadcell_D.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_D.get_weight_mean(1)} grams...{newton_mean_d} newtons...at time: {time_conversion(time_elapsed)}")
                capsule_d_list.append([time_conversion(time_elapsed), loadcell_D.get_weight_mean(1)])
            
def read_data(motor_name, duration):        #function that lets load cells read data
    print('Current weight on the scale in grams and force in Newtons is: ')
    time_target = float(duration)
    start_time = time.time()

    time_elapsed = 0
    match motor_name[-1]:
        case 'A':
            while True:
                if motor_a_lc_flag.is_set() or time_elapsed >= time_target:
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_a = ((loadcell_A.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_A.get_weight_mean(1)} grams...{newton_mean_a}...at time: {time_conversion(time_elapsed)}")
                capsule_a_list.append([time_conversion(time_elapsed), loadcell_A.get_weight_mean(1)])
       
        case 'B':
            while True:
                if motor_b_lc_flag.is_set() or time_elapsed >= time_target:
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_b = ((loadcell_B.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_B.get_weight_mean(1)} grams...{newton_mean_b} newtons...at time: {time_conversion(time_elapsed)}")
                capsule_b_list.append([time_conversion(time_elapsed), loadcell_B.get_weight_mean(1)])
        
        case 'C':
            while True:
                if motor_c_lc_flag.is_set() or time_elapsed >= time_target:
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_c = ((loadcell_C.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_C.get_weight_mean(1)} grams...{newton_mean_c} newtons...at time: {time_conversion(time_elapsed)}")
                capsule_c_list.append([time_conversion(time_elapsed), loadcell_C.get_weight_mean(1)])
        
        case 'D':
            while True:
                if motor_d_lc_flag.is_set() or time_elapsed >= time_target:
                    break
                end_time_increment = time.time()
                time_elapsed = end_time_increment-start_time
                newton_mean_d = ((loadcell_D.get_weight_mean(1)/1000)*9.81)
                print(f"{motor_name}: {loadcell_D.get_weight_mean(1)} grams...{newton_mean_d} newtons...at time: {time_conversion(time_elapsed)}")
                capsule_d_list.append([time_conversion(time_elapsed), loadcell_D.get_weight_mean(1)])
            
def start_measuring(motor_name):        #function to start reading data from specific load cell
    match motor_name[-1]:
        case 'A':
            thread_a_lc.start()
        case 'B':
            thread_b_lc.start()
        case 'C':
            thread_c_lc.start()
        case 'D':
            thread_d_lc.start()

def stop_measuring(motor_name):     #function to stop measuring data from specific load cell
    match motor_name[-1]:
        case 'A':
            motor_a_lc_flag.set()
        case 'B':
            motor_b_lc_flag.set()
        case 'C':
            motor_c_lc_flag.set()
        case 'D':
            motor_d_lc_flag.set()

def clear_flag(motor_name):     #function to clear load cell flag - only called in run_motor_wave --special case
    match motor_name[-1]:
        case 'A':
            motor_a_lc_flag.clear()
        case 'B':
            motor_b_lc_flag.clear()
        case 'C':
            motor_c_lc_flag.clear()
        case 'D':
            motor_d_lc_flag.clear()

# function to run a motor depending on type of test (compression/tensile) - used for constant and randomized strain
def run_motor_constant(motor_name, test_type, strain_type, strain_value, time_duration, stop_flag): 
    GPIO.output(motor_dict[motor_name[-1]]['enable_pin'], GPIO.HIGH)
    if test_type=='Compression Test':                                                               #TODO: have a way to convert time duration to something equivalent to control or sleep motors 
        starting_rotation = CW
        returning_rotation = CCW
    else:
        starting_rotation = CCW
        returning_rotation = CW
    
    GPIO.output(motor_dict[motor_name[-1]]['dir_pin'], starting_rotation)

    for step in range(step_conversion(strain_value)):                                           #capsule-specific motor will move in specified direction (compression or tensile) until it reaches specified linear displacement
        if stop_flag.is_set():
            break
        GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.HIGH)
        sleep(0.005)
        GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.LOW)
        sleep(0.005)
    
    if not stop_flag.is_set():
        start_measuring(motor_name)     #capsule-specific load cell will begin capturing data (get weight in grams)
        stop_flag.wait(int(time_duration))
        #sleep(int(time_duration))       #motor will hang; sample is held at specific linear-displacement for user-specified time duration
        stop_measuring(motor_name)      #after user-specified time duration passed, load cell will stop capturing data

    GPIO.output(motor_dict[motor_name[-1]]['dir_pin'], returning_rotation)
    for step in range(step_conversion(strain_value)):
        if stop_flag.is_set():
            break
        GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.HIGH)
        sleep(0.005)
        GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.LOW)
        sleep(0.005)
    
    GPIO.output(motor_dict[motor_name[-1]]['enable_pin'], GPIO.LOW)
    wx.CallAfter(jobs_frame.done_running, motor_name, test_type, strain_type)

def run_motor_wave(motor_name, test_type, strain_type, min_strain, max_strain, time_duration, stop_flag): #TODO: MAYBE TENSION AND COMPRESSION DO NOT MATTER FOR WAVE TEST...OR LET THE USER KNOW WHICH IT IS GOING FIRST, UP OR DOWN DEPENDING ON COMPRESSION OR TENSILE.ALSO HAVE AN OUTSIDE TIMER TO CALCULATE TOTAL TIME BECAUSE OTHER TIMERS ARE USED TO 
    GPIO.output(motor_dict[motor_name[-1]]['enable_pin'], GPIO.HIGH)                                                                                                    #STOP THE MOTORS AND HANG FOR LOADCELLS TO READ....OR THIS IS A TEST WHERE THE USER WILL HAVE TO STEP IN AND STOP THE TEST MANUALLY
    if test_type=='Compression Test':                                                               #TODO: have a way to convert time duration to something equivalent to control or sleep motors 
        starting_rotation = CW                                                                      #TODO: HAVE A LINE WRITTEN IN THE .CSV FILE TO DENOTE WHEN IT IS COMPRESSING OR TENSION-NING
        returning_rotation = CCW
    
    else:
        starting_rotation = CCW
        returning_rotation = CW
    
    GPIO.output(motor_dict[motor_name[-1]]['dir_pin'], starting_rotation)

    while True:
        if stop_flag.is_set():
            break
        for step in range(step_conversion(max_strain)):
            
            if stop_flag.is_set():
                break
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.HIGH)
            sleep(0.005)
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.LOW)
            sleep(0.005)

        GPIO.output(motor_dict[motor_name[-1]]['dir_pin'], returning_rotation)
        for step in range(step_conversion(max_strain)):
            if stop_flag.is_set():
                break
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.HIGH)
            sleep(0.005)
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.LOW)
            sleep(0.005)
        
        for step in range(step_conversion(min_strain)):
            if stop_flag.is_set():
                break
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.HIGH)
            sleep(0.005)
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.LOW)
            sleep(0.005)

        GPIO.output(motor_dict[motor_name[-1]]['dir_pin'], starting_rotation)
        for step in range(step_conversion(min_strain)):
            if stop_flag.is_set():
                break
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.HIGH)
            sleep(0.005)
            GPIO.output(motor_dict[motor_name[-1]]['step_pin'], GPIO.LOW)
            sleep(0.005)

    GPIO.output(motor_dict[motor_name[-1]]['enable_pin'], GPIO.LOW)
    wx.CallAfter(jobs_frame.done_running, motor_name, test_type, strain_type)


#Code source: https://github.com/gandalf15/HX711/blob/master/python_examples/example.py for load cell calibration code
#Code source: https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d
#code source: https://pypi.org/project/hx711/ 
#code source: https://github.com/mpibpc-mroose/hx711/blob/master/example.py 