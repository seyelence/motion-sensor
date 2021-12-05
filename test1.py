import RPi.GPIO as GPIO
import time

sensor = 11
buzzer = 3
ON = 1
OFF = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)                # read output from PIR
GPIO.setup(buzzer, GPIO.OUT)               # buzzer output
while True:
    time.sleep(0.1)
    i = GPIO.input(sensor)
    if i == 0:                             # if nothing sensed -> keep off
        print ("No motion", i)
        GPIO.output(buzzer, OFF)           # turn off buzzer
  
    elif i == 1:                           # if something is sensed -> turn on
        print ("Detected motion", i)
        GPIO.output(buzzer, ON)            # turn on buzzer
        time.sleep(1)
        GPIO.output(buzzer, OFF)
        time.sleep(3) 

    