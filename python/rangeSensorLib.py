import RPi.GPIO as GPIO
import time
import datetime



def measureDistance():

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
  		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
  		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	return distance

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)

def setDefaults():
	global TRIG 
	global ECHO 
	TRIG = 23
	ECHO = 24

def cleanup():
	GPIO.cleanup()

