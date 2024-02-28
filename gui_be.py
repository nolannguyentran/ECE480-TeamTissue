motor_dict = {					#dictionary containing respective step/dir pin for each motor configuration
	'A':{
		'step_pin':33,
		'dir_pin': 35
	},
	'B':{
		'step_pin':1,
		'dir_pin': 2
	},
	'C':{
		'step_pin':3,
		'dir_pin': 4
	},
	'D':{
		'step_pin':5,
		'dir_pin': 6
	},
}


def test():
    for motor in motor_dict:
    	print(motor_dict[motor]['dir_pin'])

def status(name):
    print(name)