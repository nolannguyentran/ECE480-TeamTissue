#!/usr/bin/env python3
#import RPi.GPIO as GPIO  # import GPIO
#from hx711 import HX711  # import the class HX711

# -------------lOAD CELL CONFIGURATION--------------------------------------------------------------------------------
# SET UP LOAD CELLS BASED ON THEIR GPIO PINS


loadcell_dict = {					#dictionary containing respective step/dir pin for each load cell configuration
	'A':{
		'dout_pin': 7,               #data pin
		'pd_sck_pin': 11,            #clock pin
		'channel': 'A',
		'gain': 64,
        'num_readings': 10
	},
	'B':{
		'dout_pin':22,
		'pd_sck_pin': 18,
		'channel': 'B',
		'gain': 64, 
        'num_readings': 10
	},
	'C':{
		'dout_pin': 15,
		'pd_sck_pin': 13,
		'channel': 'C',
		'gain': 64,
        'num_readings': 10
	},
	'D':{
		'dout_pin':24,
		'pd_sck_pin': 26,
		'channel': 'D',
		'gain': 64,
        'num_readings': 10
	},
}
