from time import sleep
import RPi.GPIO as GPIO


#Config for stepper motor 1
DIR_PIN_S1 = 29        # Direction GPIO Pin motor 1
STEP_PIN_S1 = 27       # Step GPIO Pin motor 1 
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise
SPR = 202       # Steps per Revolution (365 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN_S1, GPIO.OUT)
GPIO.setup(STEP_PIN_S1, GPIO.OUT)
GPIO.output(DIR_PIN_S1, CW)    #set initial rotation to cw

step_count = SPR    #rotation
delay = 0.005       # 1 sec / 202

for i in range(step_count):
    GPIO.output(STEP_PIN_S1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP_PIN_S1, GPIO.LOW)
    sleep(delay)

sleep(0.5)
GPIO.output(DIR_PIN_S1, CCW)   #set rotation to ccw
for i in range(step_count):
    GPIO.output(STEP_PIN_S1, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP_PIN_S1, GPIO.LOW)
    sleep(delay)




#Code source: https://www.youtube.com/watch?v=LUbhPKBL_IU
