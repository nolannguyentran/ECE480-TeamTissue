import RPi.GPIO as GPIO
from hx711 import HX711

# -------------lOAD CELL CONFIGURATION FILE: SET UP LOAD CELLS BASED ON THEIR GPIO PINS & IN RELATION TO MOTORS -------------------------------------------------
#motor a = load cell a....etc

loadcell_dict = {					#dictionary containing respective step/dir pin for each motor configuration
	'A':{
		'dout_pin':5,               #data pin
		'pd_sck_pin': 6,            #clock pin
		'channel': 'A',
		'gain': 64,
        'num_readings': 10
	},
	'B':{
		'dout_pin':1,
		'pd_sck_pin': 2,
		'channel': 'A',
		'gain': 64, 
        'num_readings': 10
	},
	'C':{
		'dout_pin':3,
		'pd_sck_pin': 4,
		'channel': 'A',
		'gain': 64,
        'num_readings': 10
	},
	'D':{
		'dout_pin':7,
		'pd_sck_pin': 8,
		'channel': 'A',
		'gain': 64,
        'num_readings': 10
	},
}

# function to initialize channel, gain, and setup pins for loadcell 1-4
def initialize_loadcells():
    global loadcell_A
    global loadcell_B
    global loadcell_C
    global loadcell_D

    loadcell_A = HX711(dout_pin=loadcell_dict['A']['dout_pin'], pd_sck_pin=loadcell_dict['A']['pd_sck_pin'], channel=loadcell_dict['A']['channel'], gain=loadcell_dict['A']['gain']) 
    loadcell_B = HX711(dout_pin=loadcell_dict['B']['dout_pin'], pd_sck_pin=loadcell_dict['B']['pd_sck_pin'], channel=loadcell_dict['B']['channel'], gain=loadcell_dict['B']['gain']) 
    loadcell_C = HX711(dout_pin=loadcell_dict['C']['dout_pin'], pd_sck_pin=loadcell_dict['C']['pd_sck_pin'], channel=loadcell_dict['C']['channel'], gain=loadcell_dict['C']['gain']) 
    loadcell_D = HX711(dout_pin=loadcell_dict['D']['dout_pin'], pd_sck_pin=loadcell_dict['D']['pd_sck_pin'], channel=loadcell_dict['D']['channel'], gain=loadcell_dict['D']['gain']) 

    loadcell_A.reset()
    loadcell_B.reset()
    loadcell_C.reset()
    loadcell_D.reset()

def read_data(motor_name):
    match motor_name:
        case 'A':
            loadcell_A.get_raw_data(loadcell_dict[motor_name]['num_readings'])
        case 'B':
            loadcell_B.get_raw_data(loadcell_dict[motor_name]['num_readings'])
        case 'C':
            loadcell_C.get_raw_data(loadcell_dict[motor_name]['num_readings'])
        case 'D':
            loadcell_D.get_raw_data(loadcell_dict[motor_name]['num_readings'])


#GPIO.cleanup() -----------------------------------------------------> might add this line everytime close test
#code source: https://pypi.org/project/hx711/ 
#code source: https://github.com/mpibpc-mroose/hx711/blob/master/example.py 