import RPi.GPIO as GPIO
import time
import json
import os
import ibmiotf.application
import uuid

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(32, GPIO.IN)         #Read output from PIR motion sensor

basetime = time.time()
n = 0

while True:
	i=GPIO.input(32)
	if i == 1:
		n += 1
	elif i == 0:
		n = 0
	print i, n
	time.sleep(1)
