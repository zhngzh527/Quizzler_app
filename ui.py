from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Arial",20,"italic")

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_label =Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.text = self.canvas.create_text(150,120,text= "text",font=FONT,fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image,highlightthickness=0)
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)


        self.window.mainloop()

