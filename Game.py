import tkinter as tk
from random import randint
from PIL import ImageTk
class Game(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.body()
        self.screen2(self.play)
        self.dice_images = {
            n: ImageTk.PhotoImage(file=f'images/dice{n}.png')
            for n in range(1, 7)
        }
        self.roll_item = None
        self.roll_photo = None
        #self.pack()
    def body(self):
        self.canvas = tk.Canvas(self.master)
        self.canvas['width'] = 487
        self.canvas['height'] = 487
        self.canvas['bd'] = -2
        self.canvas.pack()
        self.background_img = ImageTk.PhotoImage(file='images/stars.jpg')
        self.canvas.create_image(450,243,anchor='center',image=self.background_img)
    def screen(self):
        self.frame = tk.LabelFrame(self.master,bg='green',bd=-2)
        self.frame.place(
            relx=.1,rely=.1,relwidth=.8,relheight=.67)
    def screen2(self,show):
        self.Image = ImageTk.PhotoImage(file='images/Untitled.png')
        self.frame2 = tk.Button(self.master,image=self.Image,bg='white',bd=-2,fg="white",command=show,font='Helvetica 16 bold',text="Roll")
        self.frame2.place(relx=.43,rely=.8,relwidth=.12,relheight=.11)
        #self.create_widgets()
    def randomDiceRoll(self):
        return randint(1, 6)

    def play(self):
        number = self.randomDiceRoll()
        if self.roll_item is not None:
            self.canvas.delete(self.roll_item)
        self.roll_photo = self.dice_images[number]
        self.roll_item = self.canvas.create_image(
            243.5, 243.5,
            anchor='center',
            image=self.roll_photo
        )

root = tk.Tk()
root.resizable(False,False)
root.title('Rolling Die')
app = Game(root)
app.mainloop()