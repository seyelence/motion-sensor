import RPi.GPIO as GPIO
import time

sensor = 11              # Pin GPIO17
buzzer = 3                   # Pin GPIO4

# setmode allows us to set the numbering we use for our pins

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)
current_state = 0

# can cancel with ctrl + c on terminal
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(sensor)
        if current_state == 1:
            print("Motion has been detected", current_state)
            GPIO.output(buzzer, True)                        # alarm on
            time.sleep(1)
            GPIO.output(buzzer,False)                        # alarm off
            time.sleep(3)
        elif current_state == 0:                             # if nothing sensed -> keep off
            print("No motion", current_state)
            GPIO.output(buzzer, False) 
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
