import RPi.GPIO as GPIO
import time

sensor = 11              # Pin GPIO17
buzzer = 3               

# setmode allows us to set the numbering we use for our pins

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)                                     # read input from PIR
GPIO.setup(buzzer, GPIO.OUT)                                    # buzzer output
current_state = 0                                               # represents if there's motion or not

# can cancel with ctrl + c on terminal
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(sensor)
        if current_state == 1:                                  # if something is sensed -> turn on
            print("Motion has been detected", current_state)
            GPIO.output(buzzer, True)                           # turn on buzzer
            time.sleep(1)
            GPIO.output(buzzer,False)                           # turn off buzzer
            time.sleep(3)
        elif current_state == 0:                                # if nothing sensed -> keep off
            print("No motion", current_state)
            GPIO.output(buzzer, False) 
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
