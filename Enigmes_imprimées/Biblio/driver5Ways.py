#coding : utf-8
import smbus
from Biblio.grovepi import *
from time import *


bus = smbus.SMBus(1)

#Retourne la direction lu par le capteur
#0 : bas, 1: droite, 2: haut, 3: gauche, 4 centre, 5: erreur de lecture 
def read5ways ():
	sleep(0.1)
	lect = read_i2c_block(0x03)
	if (lect[3] == 128):
		button = lect[4:9]
		if button[0] == 0:
			return 1 #bas 
		elif button[1] == 0:
			return 2 #droite
		elif button[2] == 0: 
			return 3 #haut
		elif button[3] == 0:
			return 4 #gauche 
		elif button[4] == 0:
			return 5 #centre
		else:
			return 0
	else:
		return 0



def valeurSwitch():
		val = read5ways()
		options = { 1 : "bas", 2 : "droite", 3 : "haut", 4 : "gauche", 5 : "centre"}
		return options[val]()