import RPI.GPIO as GPIO
import time

pir_sensor = 11 # Pin GPIO17
piezo = 7	# Pin GPIO4

# setmode allows us to set the numbering we use for our pins

GPIO.setmode(GPIO.BOARD)
GPIO.setup(piezo,GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)
current_state = 0

# can cancel with ctrl + c on terminal
try:
    while True:
        time.sleep(0.1)
        # sensor checks for motion
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("Motion has been detected. GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(piezo,True)		    # alarm on
            time.sleep(1)
            GPIO.output(piezo,False)    	# alarm on
            time.sleep(5)               
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
