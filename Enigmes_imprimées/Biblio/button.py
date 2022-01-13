#can be used for button. mech keycap(only button part), touch sensor
from Biblio.grovepi import *

def initButton(pin):
	pinMode(pin,"INPUT")
	return 1 

def readButton(pin):
	return digitalRead(pin)
	
