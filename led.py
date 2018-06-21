import RPi.GPIO as GPIO

class Pin:

    def __init__(self, number):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.number = number
        self.state = False

class Led(Pin):

    pass
