"""
This example shows connecting to the PN532 and writing an M1
type RFID tag

Warning: DO NOT write the blocks of 4N+3 (3, 7, 11, ..., 63)
or else you will change the password for blocks 4N ~ 4N+2.

Note: 
1.  The first 6 bytes (KEY A) of the 4N+3 blocks are always shown as 0x00,
since 'KEY A' is unreadable. In contrast, the last 6 bytes (KEY B) of the 
4N+3 blocks are readable.
2.  Block 0 is unwritable. 
"""
import RPi.GPIO as GPIO

import pn532.pn532 as nfc
from pn532 import *


#pn532 = PN532_SPI(debug=False, reset=20, cs=4)
pn532 = PN532_I2C(debug=False, reset=20, req=16)
#pn532 = PN532_UART(debug=False, reset=20)

ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()

print('Waiting for RFID/NFC card to write to!')
while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    print('.', end="")
    # Try again if no card is available.
    if uid is not None:
        break
print('Found card with UID:', [hex(i) for i in uid])

"""
Warning: DO NOT write the blocks of 4N+3 (3, 7, 11, ..., 63)
or else you will change the password for blocks 4N ~ 4N+2.

Note: 
1.  The first 6 bytes (KEY A) of the 4N+3 blocks are always shown as 0x00,
since 'KEY A' is unreadable. In contrast, the last 6 bytes (KEY B) of the 
4N+3 blocks are readable.
2.  Block 0 is unwritable.
"""

writableLines = [1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30,32,33,34,36,37,38,40,41,42,44,45,46,48,49,50,52,53,54,56,57,58,60,61,62]
##16 char par ligne

# 16 blocks
blocks = [[1,2],[4,5,6],[8,9,10],[12,13,14],[16,17,18],[20,21,22],[24,25,26],[28,29,30],[32,33,34],[36,37,38],[40,41,42],[44,45,46],[48,49,50],[52,53,54],[56,57,58],[60,61,62]]

'''
# Write block #6
block_number = 6
key_a = b'\xFF\xFF\xFF\xFF\xFF\xFF'
data = bytes([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F])

try:
    pn532.mifare_classic_authenticate_block(
        uid, block_number=block_number, key_number=nfc.MIFARE_CMD_AUTH_A, key=key_a)
    pn532.mifare_classic_write_block(block_number, data)
    if pn532.mifare_classic_read_block(block_number) == data:
        print('write block %d successfully' % block_number)
except nfc.PN532Error as e:
    print(e.errmsg)
GPIO.cleanup()
'''

#Id secret
#96e28113b50ff25621e63730785ad0c9

def writeLine(i):
    # Write block #6
    block_number = i
    if i in writableLines:
        key_a = b'\xFF\xFF\xFF\xFF\xFF\xFF'
        data = bytes([0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F])

        try:
            pn532.mifare_classic_authenticate_block(
                uid, block_number=block_number, key_number=nfc.MIFARE_CMD_AUTH_A, key=key_a)
            pn532.mifare_classic_write_block(block_number, data)
            if pn532.mifare_classic_read_block(block_number) == data:
                print('write block %d successfully' % block_number)
        except nfc.PN532Error as e:
            print(e.errmsg)
        GPIO.cleanup()
    
writeLine(2)

def resetAllData():
    for i in writableLines:
        block_number = i
        key_a = b'\xFF\xFF\xFF\xFF\xFF\xFF'
        data = bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

        try:
            pn532.mifare_classic_authenticate_block(
                uid, block_number=block_number, key_number=nfc.MIFARE_CMD_AUTH_A, key=key_a)
            pn532.mifare_classic_write_block(block_number, data)
            if pn532.mifare_classic_read_block(block_number) == data:
                print('write block %d successfully' % block_number)
        except nfc.PN532Error as e:
            print(e.errmsg)
        GPIO.cleanup()

#def writeBlock():

resetAllData()