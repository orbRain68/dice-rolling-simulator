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
        self.num_dice = 1
        self.roll_items = []
        self.roll_photos = []
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
        self.btn_plus = tk.Button(self.master, text="+", font='Helvetica 14 bold', command=self.increase_dice)
        self.btn_plus.place(relx=.56, rely=.8, relwidth=.05, relheight=.11)

        self.btn_minus = tk.Button(self.master, text="-", font='Helvetica 14 bold', command=self.decrease_dice)
        self.btn_minus.place(relx=.37, rely=.8, relwidth=.05, relheight=.11)
        #self.create_widgets()
    def increase_dice(self):
        if self.num_dice < 2:
            self.num_dice += 1
            self.play()

    def decrease_dice(self):
        if self.num_dice > 1:
            self.num_dice -= 1
            self.play()
    def randomDiceRoll(self):
        return randint(1, 6)

    def play(self):
        for item in self.roll_items:
            self.canvas.delete(item)
        self.roll_items.clear()
        self.roll_photos.clear()

        canvas_width = 487
        spacing = canvas_width / (self.num_dice + 1)

        for i in range(self.num_dice):
            number = self.randomDiceRoll()
            photo = self.dice_images[number]
            self.roll_photos.append(photo)
            
            x_pos = spacing * (i + 1)
            item = self.canvas.create_image(
                x_pos, 253.5,
                anchor='center',
                image=photo
            )
            self.roll_items.append(item)

root = tk.Tk()
root.resizable(False,False)
root.title('Rolling Die')
app = Game(root)
app.mainloop()