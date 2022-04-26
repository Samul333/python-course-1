from tkinter import Button, Label
import random 
import settings

class Cell:
    all = []
    cell_count_label_object = None
    def __init__(self,x,y,is_mine =False) -> None:
        self.is_mine = is_mine
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
        
    def show_mine(self):
        # A logic do interrupt the game and display a message that player lost!
        self.cell_btn_object.configure(bg='red')
    
    
    def get_cell_by_axis(self,x,y):
        #Return a cell object based on the value of x and y
        
        for cell in Cell.all:
            if cell.x  == x and cell.y == y:
                return cell
            
    @property            
    def surrounded_cells(self):
        surrounded_cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1),
         ]
        
        cells = [cell for cell in surrounded_cells if cell]
        
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
    
    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
    
    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
    
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