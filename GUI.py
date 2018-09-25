import RPi.GPIO as GPIO
import tkinter as tk


class RpiGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

class PinButton(tk.Button):
    def __init__(self, parent, pin, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pin = pin
    
if __name__ == '__main__':
    root = tk.Tk()
    RpiGUI(root)
    root.mainloop()
#GPIO.setmode(GPIO.BCM)
#channel = 5
#GPIO.setup(channel, GPIO.OUT)
#print(GPIO.input(channel))
