from Biblio.driver5Ways import *
from Biblio.LED import *
import os
import time
from driverI2C import *

os.system("sudo echo -e '\nLa troisieme enigme va vous être\n donnée\n\n\n' > /dev/usb/lp0")

time.sleep(3)

#enigme pour FASE
os.system("sudo echo -e '\nLa premiere enigme va vous être\n donnée\n\n\n' > /dev/usb/lp0")

time.sleep(4)

#impression enigme FASE
os.system("sudo echo -e 'Vous voulez continuer la suite\ndes enigmes, mais le problème\nest que l'ordinateur contenant\nle programme n'a plus d'écran\nni de clavier.\n Mais c'est votre jour de chance,\nil y a un deuxieme ordinateur\ndans la pièce (raspberry).\nUtilisez-le et faites des\nmanipulations dans le terminal\n à l'aide de l'écran et du\nclavier.\nVous allez devoir vous connecter\nsur l'ordinateur cassée avec\nles identifiants que vous\ntrouverez dans la pièce.\nTransferez l'archive sur\nl'ordinateur que vous utilisez.\nDésarchivez-la, et executez le\nmain grace au terminal\n(programme python).\n\n\n' > /dev/usb/lp0")

time.sleep(3)

os.system("sudo echo -e 'Vous avez de la chance,on vous\ndonne le  prochain indice en\navance : 4R\n\n\n' > /dev/usb/lp0")