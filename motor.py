from time import sleep
import RPi.GPIO as GPIO


#Config for stepper motor 1
DIR = 20        # Direction GPIO Pin
STEP = 21       # Step GPIO Pin
CW = 1          # Clockwise 
CCW = 0         # CounterClockwise
SPR = 202       # Steps per Revolution (365 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)    #set initial rotation to cw

step_count = SPR    #rotation
delay = 0.005       # 1 sec / 202

for i in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(0.5)
GPIO.output(DIR, CCW)   #set rotation to ccw
for i in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)




#Code source: https://www.youtube.com/watch?v=LUbhPKBL_IU
