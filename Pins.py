try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    import RPi_GPIO_ as GPIO
    
def get_board():
    board = [['3v3', Pin(2, 'SDA'), Pin(3, 'SCL'), Pin(4, 'GPCLK0'),
             'Ground', Pin(17, ''), Pin(27, ''), Pin(22, ''), '3v3',
             Pin(10, 'MOSI'), Pin(9, 'MISO'), Pin(11, 'SCLK'), 'Ground',
             Pin(0, 'ID_SD'), Pin(5, ''), Pin(6, ''), Pin(13, 'PWM1'),
             Pin(19, 'MISO'), Pin(26, ''), 'Ground'],
             ['5v Power', '5v Power', 'Ground', Pin(14, 'TXD'),
              Pin(15, 'RXD'), Pin(18, 'PWM0'), 'Ground', Pin(23, ''),
              Pin(24, ''), 'Ground', Pin(25, ''), Pin(8, 'CE0'),
              Pin(7, 'CE1'), Pin(1, 'ID_SC'), 'Ground', Pin(12, 'PWM0'),
              'Ground', Pin(16, ''), Pin(20, 'MOSI'), Pin(21, 'SCLK')]]
    return board
class Pin:
    
    def __init__(self, number, special):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(number,GPIO.OUT)
        self.number = number
        self.state = False
        self.special = special
    
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
        if number in range(0, 28):
            self._number = number
        else:
            raise ValueError
