import RPi.GPIO as GPIO
import tkinter as tk
from led import Pin

class RpiGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid(column=2, row=20)
        self.but = PinButton(self,Pin(5))
        self.but.grid(column=2, row=1)
        self.but2 = PinButton(self,Pin(6))
        self.but2.grid(column=1, row=1)
        

class PinButton(tk.Button):
    def __init__(self, parent, pin, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pin = pin
        self.configure(command=self.pressed,background='gray', text='Off')
    def pressed(self):
        self.pin.change_state()
        if self.pin.state:
            self.config(background='green', text='On')
        else:
            self.config(background='gray', text='Off')
    
if __name__ == '__main__':
    root = tk.Tk()
    RpiGUI(root)
    root.mainloop()
#GPIO.setmode(GPIO.BCM)
#channel = 5
#GPIO.setup(channel, GPIO.OUT)
#print(GPIO.input(channel))
