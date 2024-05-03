# -------------LOAD CELL CONFIGURATION--------------------------------------------------------------------------------
# SET UP LOAD CELLS BASED ON THEIR GPIO PINS


loadcell_dict = {					#dictionary containing respective step/dir pin for each load cell configuration
	'A':{
		'dout_pin': 7,               #data pin
		'pd_sck_pin': 11             #clock pin
	},
	'B':{
		'dout_pin':22,
		'pd_sck_pin': 18
	},
	'C':{
		'dout_pin': 15,
		'pd_sck_pin': 13
	},
	'D':{
		'dout_pin':24,
		'pd_sck_pin': 26
	},
}
