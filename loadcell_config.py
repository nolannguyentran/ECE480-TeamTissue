#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

# -------------lOAD CELL CONFIGURATION--------------------------------------------------------------------------------
# SET UP LOAD CELLS BASED ON THEIR GPIO PINS


loadcell_dict = {					#dictionary containing respective step/dir pin for each load cell configuration
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




try:
    GPIO.setmode(GPIO.BOARD)  # set GPIO pin mode to BCM numbering
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
    hx = HX711(dout_pin=24, pd_sck_pin=26)
    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128
    err = hx.zero()
    # check if successful
    if err:
        raise ValueError('Tare is unsuccessful.')

    reading = hx.get_raw_data_mean()
    if reading:  # always check if you get correct value or only False
        # now the value is close to 0
        print('Data subtracted by offset but still not converted to units:',
              reading)
    else:
        print('invalid data', reading)

    # In order to calculate the conversion ratio to some units, in my case I want grams,
    # you must have known weight.
    input('Put known weight on the scale and then press Enter')
    reading = hx.get_data_mean()
    if reading:
        print('Mean value from HX711 subtracted by offset:', reading)
        known_weight_grams = input(
            'Write how many grams it was and press Enter: ')
        try:
            value = float(known_weight_grams)
            print(value, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:',
                  known_weight_grams)

        # set scale ratio for particular channel and gain which is
        # used to calculate the conversion to units. Required argument is only
        # scale ratio. Without arguments 'channel' and 'gain_A' it sets
        # the ratio for current channel and gain.
        ratio = reading / value  # calculate the ratio for channel A and gain 128
        hx.set_scale_ratio(ratio)  # set ratio for current channel
        print('Ratio is set.')
    else:
        raise ValueError('Cannot calculate mean value. Try debug mode. Variable reading:', reading)

    # Read data several times and return mean value
    # subtracted by offset and converted by scale ratio to
    # desired units. In my case in grams.
    print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
    input('Press Enter to begin reading')
    print('Current weight on the scale in grams and force in Newtons is: ')
    while True:
        print(hx.get_weight_mean(20), 'g')
        
        #convert grams to newtons
        newton_mean = ((hx.get_weight_mean(20) / 1000) * 9.81)

        print(newton_mean, 'N')

except (KeyboardInterrupt, SystemExit):
    print('Bye :)')

finally:
    GPIO.cleanup()