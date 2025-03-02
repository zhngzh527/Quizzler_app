from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas = Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.text = self.canvas.create_text(150,120,text= "text",font=FONT)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image,highlightthickness=0)
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)


        self.window.mainloop()

