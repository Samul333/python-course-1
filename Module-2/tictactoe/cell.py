from tkinter import Button, Label
import random 
import settings

class Cell:
    all = []
    cell_count_label_object = None
    move = 0
    def __init__(self,x,y,is_mine =False) -> None:
        self.state = -1
        self.x = x
        self.y = y
        self.cell_btn_object = None
        
        # Append the object to the Cell.all list
        Cell.all.append(self)
        
    
    def create_btn_object(self,location):
        btn = Button(
            location,
            width=12,
            height=4,
            text='',
        )
        btn.bind('<Button-1>',self.left_click)
        btn.bind('<Button-3>',self.right_click)
        
        self.cell_btn_object = btn
        
    
    
    def get_cell_by_axis(self,x,y):
        #Return a cell object based on the value of x and y
        
        for cell in Cell.all:
            if cell.x  == x and cell.y == y:
                return cell
            
    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
    
    def left_click(self,event):
        if Cell.move == 0:
            self.cell_btn_object.configure(text='X')
            self.state = 1
            Cell.move = 1
        else:
            Cell.move = 0
            self.state = 0
            self.cell_btn_object.configure(text='O')
        
        self.check_win()
    
    
    def paint_green(self,cells):
        for cell in cells:
                cell.cell_btn_object.configure(bg='lightgreen')
    
    def check_win(self):
        win =False
        for i in range(3):
            states = []
            cells_list = []
            for j in range(3):
                cell = self.get_cell_by_axis(i,j)
                states.append(cell.state)
                cells_list.append(cell)
            
            if states == [1,1,1]:
                win = True
                self.paint_green(cells_list)
                break
            elif states == [0,0,0]:
                win = True
                self.paint_green(cells_list)
                break
        
        for i in range(3):
            states = []
            cells_list = []
            for j in range(3):
                cell = self.get_cell_by_axis(j,i)
                states.append(cell.state)
                cells_list.append(cell)
                
            if states == [1,1,1]:
                win = True
                self.paint_green(cells_list)
                break
            elif states == [0,0,0]:
                win = True
                self.paint_green(cells_list)
                break
        
        states =   []    
        for i in range(3):
         
            cell = self.get_cell_by_axis(i,i)
            states.append(cell.state)
            if states == [1,1,1]:
                win = True
                break
            elif states == [0,0,0]:
                win = True
                break
            
        states =   []
        
        for i in range(3):
            cell = self.get_cell_by_axis(i,3-i-1)
            states.append(cell.state)
            if states == [1,1,1]:
                win = True
                break
            elif states == [0,0,0]:
                win = True
                break
        
        if win == True:
             print('You win')
            
            
        states 

    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            width=12,
            height=4,
            bg='black',
            fg='white',
            font=("",30),
            text=f'Cells count: {settings.CELL_COUNT}',
        )
        
        Cell.cell_count_label_object = lbl
    
    def right_click(self,event):
        print(event)
        print("I am right click ")
     
    
    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all,settings.MINES_COUNT
        )  
        
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    
    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"