from Biblio.driver5Ways import *
from Biblio.LED import *
from driverI2C import *
import os
import time
import random


os.system("sudo echo -e 'La deuxième enigme va vous être\n donnée.Elle va porter \nsur les cours d'Algo\n\n' > /dev/usb/lp0")

time.sleep(5)

#Commande pour imprimer le problème d'algo

os.system("sudo echo -e 'func fonction1(y : Int)->Bool{\n    compt : Bool = True\n    i : Int = 2\n    while i<y && compt{\n	if(y%i == 0){\n	    compt = False\n	}\n    i += 1\n    }\n    return compt\n}\n\n\nfunc fonction2(x : Int)->Int{\n    var i : Int = 0\n    var t : Int = 0\n    for i in 1..<x{\n       if(fonction1(i)){\n          t += i\n       }\n        }\n    return t\n}\n\nfonction2(x : 10)\n\n\n\n' > /dev/usb/lp0")

os.system("sudo echo -e 'Quel résultat va retourner cet\n algorithme?\n\n' > /dev/usb/lp0")

time.sleep(2)

os.system("sudo echo -e 'Vers le haut :   16\nVers le bas :     3\nVers la droite : 21\nVers la gauche : 18\n\n\n' > /dev/usb/lp0")

time.sleep(1)

os.system("sudo echo -e '\nConfirmez votre choix en cliquant au\n centre\n\n\n' > /dev/usb/lp0")

setText("Pensez-vous y    arriver ?")

position = -1    #permet de stocker un choix si la valeur retournée par le bouton respecte les contraintes, position vaut -1 par défaut, cela veut dire que aucune position valide n'a encore été saisie
positionValide = False  #Permet de savoir si on a pris le choix de valider une position. Ne peut pas être égale à True si position = -1
fin = True
while fin:
    val = read5ways()
    if(val != 0 and val != 5): #Si haut, bas, gauche ou droite
        position = val
        setText("Vous pouvez     confirmer")
        continue
    if(val == 5 and position != -1): #Confirmation et une réponse déjà donnée ?
        if(position == 4): #C'est la bonne réponse(vers la gauche)
            setColor("bleu")
            setText("C'est la bonne  reponse!!!")
            fin = False
            time.sleep(1.5)
            setColor("vert")
        else:
            setColor("rouge")
            setText("Mauvaise reponse!")
            positionValide = False
            position = -1
            time.sleep(2)
            setColor("vert")
            setText("Reessayez!")
        continue
    if(val != 0):
        setText("Veuillez choisir une valeur")

setText("")

os.system("sudo echo -e '\nBien joué !\nVoici un indice à noter: 3 R\n\n\n' > /dev/usb/lp0")

for i in range(100):
    setRGB(random.randint(0,255),random.randint(0,255),random.randint(0,255))

setColor("vert")