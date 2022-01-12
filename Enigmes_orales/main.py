# coding: utf-8

import time
from random import *
import speech_recognition as sr
import soundfile as sf
import sounddevice as sd
import RPi.GPIO as GPIO
from Biblio.python_pn532.pn532 import *

# JOUER UN SON
data, fs = sf.read('annonce_anglais.wav', dtype = 'float32')
sd.play(data, fs)
sd.wait()

not_ended = True
while not_ended:
    r = sr.Recognizer()
    micro = sr.Microphone()
    #setText("Allez-y !")
    with micro as source:
        print("Parle !")
        audio_data = r.listen(source)
        print("FIN !")
    result = r.recognize_google(audio_data, language="en-EN")
    print(result)
    #setText(result)
    if "1234567" in result:
        print("Yes it does")
        not_ended = False
        #setText("Yes it does")
    else:
        print("No it doesn't")
        #setText("No it doesn't")

data, fs = sf.read('win_anglais.wav', dtype = 'float32')
sd.play(data, fs)
sd.wait()

time.sleep(1.5)

data, fs = sf.read('annonce_NFC.wav', dtype = 'float32')
sd.play(data, fs)
sd.wait()

try:
    pn532 = PN532_I2C(debug=False, reset=20, req=16)
    # Configure PN532 to communicate with MiFare cards
    pn532.SAM_configuration()
    print('Waiting for RFID/NFC card...')
    not_ended = True
    while not_ended:
        # Check if a card is available to read
        uid = pn532.read_passive_target(timeout=0.5)
        print('.', end="")
        # Try again if no card is available.
        if uid is None:
            continue
        entire_UID = [hex(i) for i in uid]
        print('Found card with UID:', entire_UID)
        if entire_UID == ['0x1f', '0xf5', '0x90', '0x0']:           # If the correct NFC card has been passed
            not_ended = False
            data, fs = sf.read('win_nfc.wav', dtype = 'float32')    # Give the letter orally
            sd.play(data, fs)
            sd.wait()
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
