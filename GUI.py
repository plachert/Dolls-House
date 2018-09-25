import RPi.GPIO as GPIO
import tkinter as tk


class RpiGUI(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self*args, **kwargs)
#GPIO.setmode(GPIO.BCM)
#channel = 5
#GPIO.setup(channel, GPIO.OUT)
#print(GPIO.input(channel))
