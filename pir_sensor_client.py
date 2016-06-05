import RPi.GPIO as GPIO
import time
import json
import os
import ibmiotf.application
import uuid

client = None

try:
	options = ibmiotf.application.ParseConfigFile("/home/pi/player_count/device.cfg")
	options["deviceid"] = options["id"]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(32, GPIO.IN)         #Read output from PIR motion sensor

def appendUnique(lst, x):
	if x not in lst:
		lst.append(x)
	return lst

counter = 0

while True:
	i=GPIO.input(7)
	j=GPIO.input(32)
	tmp = []
	print i,j
	if i == 0 and j == 0:
		while True:
			i=GPIO.input(7)
			j=GPIO.input(32)
			if len(tmp) < 2:
				if i == 1 or j == 1:
					if tmp:
						if i == 1 and tmp[0] != "i":
							tmp = appendUnique(tmp, "i")
						elif j == 1 and tmp[0] != "j":
							tmp = appendUnique(tmp, "j")
					else:
						if i == 1:
							tmp = appendUnique(tmp, "i")
						elif j == 1:
							tmp = appendUnique(tmp, "j")
			elif len(tmp) == 2:
				print(tmp)
				if tmp[0] == "i":
					print "ENTER"
					counter += 1
					break
				else:
					print "EXIT"
					counter -= 1
					break
			else:
				print "WTF" 							 
	else:
		print "sensors are not at 0"
		print "counter is at ", counter
	jsonData = json.dumps(counter)
	print jsonData
	time.sleep(1)
