
import tkinter as tk
from Pins import get_board, Pin

class RpiGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid(column=5, row=20)
        #mapping board to buttons
        board = get_board()
        self.board = []
        #left side
        for i in range(len(board[0])):
            if type(board[0][i])==Pin:
                button = PinButton(self, board[0][i])
                tk.Label(self, text=board[0][i].special).grid(column=1, row=i+1)
                
            else:
                button = NonPinButton(self, board[0][i])
            
            button.grid(column=2, row=i+1)
            self.board.append(button)
        #right side
        for i in range(len(board[1])):
            if type(board[1][i])==Pin:
                button = PinButton(self, board[1][i])
                tk.Label(self, text=board[1][i].special).grid(column=5, row=i+1)
                
            else:
                button = NonPinButton(self, board[1][i])
            
            button.grid(column=4, row=i+1)
            self.board.append(button)

        

class PinButton(tk.Button):
    def __init__(self, parent, pin, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pin = pin
        self.configure(command=self.pressed,background='gray', text='Off',
                       height = 1, width = 7)
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
        self.configure(background='gray', text=text, state=tk.DISABLED,
                       height = 1, width = 7)

if __name__ == '__main__':
    root = tk.Tk()
    RpiGUI(root)
    root.mainloop()

