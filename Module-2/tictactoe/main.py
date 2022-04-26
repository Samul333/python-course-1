import settings
from tkinter import *
from cell import Cell
from tkinter import messagebox
import utils

root = Tk()
root.title('Tic Tac Toe')

root.resizable(False,False)



for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(root)
        c.cell_btn_object.grid(row=x,column=y)




root.mainloop()



