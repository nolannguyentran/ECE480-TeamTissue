
# -------------MOTOR CONFIGURATION FILE-------------------------------------------------
# SET UP MOTORS BASED ON THEIR GPIO PINS


# number of steps per revolution = 360/motor's step angle, which 
# for the haydon motor, the step angle is 1.8 from the data sheet
# therefore the number of steps required to complete one revolution is:
# 360/1.8 = 200


motor_dict = {					#dictionary containing respective step/dir/en pin for each motor configuration
	'A':{
		'step_pin':38,
		'dir_pin': 40,
        'enable_pin': 23
	},
	'B':{
		'step_pin':32,
		'dir_pin': 36,
        'enable_pin': 21
	},
	'C':{
		'step_pin':33,
		'dir_pin': 35,
        'enable_pin': 37
	},
	'D':{
		'step_pin':29,
		'dir_pin': 31,
        'enable_pin': 19
	},
}



