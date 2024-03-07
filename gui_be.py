import motor

a = motor.motor_dict


def test():
    for motor in a:
    	print(a[motor]['dir_pin'])

def status(name):
    print(name)