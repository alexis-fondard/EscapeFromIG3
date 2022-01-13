# coding: utf-8

from Biblio.LED import *
from Biblio.button import *
from driverI2C import *
from Biblio.driver5Ways import *
import os
from Biblio.grovepi import *
import time


#pour autoriser l'accés à l'imprimante
os.system("sudo chmod a+w /dev/usb/lp0") 


#Pour initialiser le bouton 5 directions et l'écran LCD,
#voir directement dans les fichiers 'driverI2C.py' et 'driver5ways.py'

#Initialisation écriture écran LCD
setColor("vert")


#initialisation des boutons 
pinButton1 = 2
pinButton2 = 3
initButton(pinButton1)
initButton(pinButton2)


#initialisation des LEDS
pinLED1 = 6
pinLED2 = 4
initLED(pinLED1)
initLED(pinLED2)

setText("Bienvenue à vous")

time.sleep(2)

setText("Appuyez sur le bouton pour commencer")


os.system("python3 /home/pi/Salim/LEDclignotantes.py")

os.system("python3 /home/pi/Salim/Compta.py")

time.sleep(3)

os.system("sudo echo -e 'Bien joué, maintenant passons\n à la deuxième énigme\n\n\n' > /dev/usb/lp0")

setText("BIEN JOUE!")

time.sleep(2)

os.system("python3 /home/pi/Salim/algo.py")

os.system("sudo echo -e 'On vous a peut-etre sous-estimés,\npassons à la suivante \n\n' > /dev/usb/lp0")

setText("Trop facile ??   BIEN JOUE")

time.sleep(3)

os.system("python3 /home/pi/Salim/FASE.py")