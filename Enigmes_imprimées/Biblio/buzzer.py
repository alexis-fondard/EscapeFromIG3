# buzzer.py
from Biblio.grovepi import *

def initbuzzer(pin):
	pinMode(pin,"OUTPUT")
	return 1 

def setbuzzer(pin, value):
	digitalWrite(pin,value)
	return 1

def onbuzzer(pin):
	digitalWrite(pin,1)
	return 1

def offbuzzer(pin):
	digitalWrite(pin,0)
	return 1
