# coding: utf-8
import smbus
import time

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Indiquez ici les deux adresses de l'ecran LCD
# celle pour les couleurs du fond d'ecran 
# et celle pour afficher des caracteres
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

# Completez le code de la fonction permettant de choisir la couleur
# du fond d'ecran, n'oubliez pas d'initialiser l'ecran
def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur qu'on vous demande
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,bleu)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xAA)
	print("Couleur écran changée")

# Envoie  a l'ecran une commande concerant l'affichage des caracteres
# (cette fonction vous est donnes gratuitement si vous
# l'utilisez dans la fonction suivante, sinon donnez 2000€
# a la banque et allez dictement en prison :)
def textCmd(cmd):
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)
	time.sleep(0.1)

# Completez le code de la fonction permettant d'ecrire le texte recu en parametre
# Si le texte contient un \n ou plus de 16 caracteres pensez a gerer
# le retour a la ligne
def setText(texte):
	textCmd(0x01)
	textCmd(0x0F)
	textCmd(0x38)
	caractere = 0
	ecran = 0
	nb_ligne = 0
	texte_ligne = []
	for c in texte :# pour un caractere c a afficher :
		if c != "\n" :
			bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
			time.sleep(0.1)
		caractere += 1
		if nb_ligne == 1:
			texte_ligne.append(c)
		if c == "\n" or caractere > 15 :  # si on rencontre \n ou si on depasse 16 caracteres
			textCmd(0xc0) # pour passer a la ligne
			caractere = 0
			ecran += 1
			nb_ligne += 1
		if ecran == 2 :
			#time.sleep(2)
			textCmd(0x01)
			textCmd(0x0F)
			textCmd(0x38)
			setText(texte_ligne)
			ecran = 1
			texte_ligne = []
			nb_ligne = 1
	print ("texte ecrit")

def setColor(couleur):
    if couleur == "rouge" :
        setRGB(255,0,0)
    elif couleur == "vert" :
        setRGB(0,255,0)
    elif couleur == "bleu" :
        setRGB(0,0,255)
    elif couleur == "noir" :
        setRGB(0,0,0)
    elif couleur == "blanc" :
        setRGB(255,255,255)
    else :
        print("La couleur n'est pas disponible")