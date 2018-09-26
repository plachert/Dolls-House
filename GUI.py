
import tkinter as tk
from led import get_board, Pin

class RpiGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid(column=2, row=20)
        #mapping board to buttons
        board = get_board()
        self.board = []
        #left side
        for i in range(len(board[0])):
            if type(board[0][i])==Pin:
                button = PinButton(self, board[0][i])
                
            else:
                button = NonPinButton(self, board[0][i])
            
            button.grid(column=1, row=i+1)
            self.board.append(button)
        #right side
        for i in range(len(board[1])):
            if type(board[1][i])==Pin:
                button = PinButton(self, board[1][i])
                
            else:
                button = NonPinButton(self, board[1][i])
            
            button.grid(column=2, row=i+1)
            self.board.append(button)

        

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

class NonPinButton(tk.Button):
    def __init__(self, parent, text, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(background='gray', text=text)

if __name__ == '__main__':
    root = tk.Tk()
    RpiGUI(root)
    root.mainloop()
#GPIO.setmode(GPIO.BCM)
#channel = 5
#GPIO.setup(channel, GPIO.OUT)
#print(GPIO.input(channel))
