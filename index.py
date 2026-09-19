'''
File Name : index.py
Auther : Abdurazaq Hawsawi
Descreption
'''
import tkinter as tk
from PIL import ImageTk
from random import randint
def main():
    guiFunction()
def randomDiceRoll():
    return randint(1,6)

def result():
    rolled = input('Press R to roll the dice!!\t')
    if rolled == "r" or rolled == "R":
        return('you Rolled',randomDiceRoll())
def guiFunction():
    root = tk.Tk()
    root.title('Dice Rolling Game')
    
    root.resizable(False,False)

    canvas = tk.Canvas(root,bd=-2,bg='black',width=487,height=487)
    canvas.pack()
    background_img = ImageTk.PhotoImage(file='images/stars.jpg')
    canvas.create_image(450,243,anchor='center',image=background_img)
    root.mainloop()
if __name__=='__main__':
    main()