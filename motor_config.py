
# -------------MOTOR CONFIGURATION FILE: SET UP MOTORS BASED ON THEIR GPIO PINS-------------------------------------------------
#motor a = load cell a....etc

#from loadcell import LOADCELLOUTPUT1, LOADCELLOUTPUT2, LOADCELLOUTPUT3, LOADCELLOUTPUT4

# number of steps per revolution = 360/motor's step angle, which 
# for the haydon motor, the step angle is 1.8 from the data sheet
# therefore the number of steps required to complete one revolution is:
# 360/1.8 = 200


motor_dict = {					#dictionary containing respective step/dir pin for each motor configuration
	'A':{
		'step_pin':38,
		'dir_pin': 40
	},
	'B':{
		'step_pin':32,
		'dir_pin': 36
	},
	'C':{
		'step_pin':33,
		'dir_pin': 35
	},
	'D':{
		'step_pin':29,
		'dir_pin': 31
	},
}



