from Biblio.driver5Ways import *
from Biblio.LED import *
import os
import time
from driverI2C import *



pinLED1 = 4
pinLED2 = 6
initLED(pinLED1)
initLED(pinLED2)
offLED(pinLED1)
offLED(pinLED2)

os.system("sudo echo -e '\nLa premiere enigme va vous être\n donnée\n\n\n' > /dev/usb/lp0")

time.sleep(2)

#commande qui permet d'imprimer le journal
os.system("sudo echo -e '       |----02/07------|\n601    |Achats march   | 7000\n44566  |TVA sur B&S    | 1400\n   512 |      Banque   |    8400\n       |----05/07------|\n4455   |TVA à décaiss  | 1200\n   512 |      Banque   |    1200\n       |----09/07------|\n512    |Banque         | 1920\n   4457|  TVA collectée|     320\n   707 | Vente de march|    1600\n       |----13/07------|\n2183   |Mat inform     | 2000\n44562  |TVA sur immos  |  400\n404    |  Fourn d'immos|    2400\n       |----17/07------|\n401    |Fournisseur    | 1800\n   512  |      Banque   |    1800\n       |----20/07------|\n164    |Emprunts       |16000\n661    |Charges d'int  | 2000\n   512 |      Banque   |   18000\n       |----24/07------|\n626    |Frais post     | 150\n44566  |TVA sur B&S    |  30\n   512 |      Banque   |     180\n       |----29/07------|\n404    |Fourn d'immos  | 2400\n   512 |      Banque   |    2400\n       |----31/07------|\n12     |Resultat       | 50000\n   512 |      Banque   |   30000\n   106 |      Reserves |   20000\n       |_______________|\n\n\n' > /dev/usb/lp0")

time.sleep(1.5)

os.system("sudo echo -e 'Calculez la TVA (négative si\nc'est un crédit de TVA ou\npositive si c'est une TVA\nà décaisser)\n\n\n' > /dev/usb/lp0")


time.sleep(2)

os.system("sudo echo -e 'Utilisez le bouton à 5 direction\npour faire votre choix:\n\nVers le haut : -2710\nVers le bas : +1410\nVers la droite : -1510\nVers la gauche : +2710\n\n' > /dev/usb/lp0")

time.sleep(1)

os.system("sudo echo -e '\nConfirmez votre choix en cliquant au\n centre\n\n\n' > /dev/usb/lp0")

setText("Trop dur?       Abandonne")

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
        if(position == 2): #C'est la bonne réponse(vers la droite)
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

#l'indice est donné après avoir réussi à répondre
os.system("sudo echo -e '\nBien joué !\nVoici un indice à noter:  1 B\n\n\n' > /dev/usb/lp0")

onLED(pinLED1)
onLED(pinLED2)
time.sleep(2)
offLED(pinLED1)
offLED(pinLED2)