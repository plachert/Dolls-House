import RPi.GPIO as GPIO

class Pin:

    def __init__(self, number):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(number,GPIO.OUT)
        self.number = number
        self.state = False
    
    @property
    def number(self):
        return self._number
    
    def change_state(self):
        if self.state:
            GPIO.output(self.number,GPIO.LOW)
            self.state = False
        else:
            GPIO.output(self.number,GPIO.HIGH)
            self.state = True
    
    @number.setter
    def number(self, number):
        if number in range(1, 27):
            self._number = number
        else:
            raise ValueError

class Led(Pin):
    
    PINS = [5,6,16,17,22,23]
    
    @Pin.number.setter
    def number(self, number):
        if number in Led.PINS:
            self._number = number
        else:
            raise ValueError
