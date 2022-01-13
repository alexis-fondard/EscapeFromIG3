
from Biblio.LED import *
from Biblio.driver5Ways import *
import time
import random
from driverI2C import *


pinLED1 = 4
pinLED2 = 6   
initLED(pinLED2)
initLED(pinLED1)
fin = True

while fin:
    try:
        val = read5ways()
        if(val == 5):
            fin = False
        setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        onLED(pinLED1)
        onLED(pinLED2)
        time.sleep(.2)
        val = read5ways()
        if(val == 5):
            fin = False
        offLED(pinLED1)
        offLED(pinLED2)
        setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        val = read5ways()
        if(val == 5):
            fin = False
        time.sleep(.2)
    except IOError:
      print("Erreur")

