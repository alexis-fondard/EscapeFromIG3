import grovepi
class ledBuzz:
    mypin = 0

    def __init__(self, pin):
        mypin = pin
        grovepi.pinMode(pin, "OUTPUT")

    def turnOn(self):
        # print(mypin)
        grovepi.digitalWrite(self.mypin, 1)

    def turnOff(self):
        # print(mypin)
        grovepi.digitalWrite(self.mypin, 0)
