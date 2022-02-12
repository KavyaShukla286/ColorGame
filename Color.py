from tkinter import *
import random
from tkinter import messagebox

root =Tk()
root.title("Color Game")
root.geometry("380x245")
root.resizable(0,0)
root.iconbitmap('color.ico')
root.configure(bg='linen')

colors = ['Red', 'Blue', 'Pink', 'Black', 'Yellow', 'Teal','Cyan','Magenta', 'White', 'Brown','Green','Hotpink','Gray','PowderBlue','Orange','Tan']

score = 0
timeleft = 45

def startGame(event):
    if timeleft == 45:
        countdown()
    nextcolor()

def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("Time Over ", "Your Score is "+str(score))
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time Left : " +str(timeleft))
        timeLabel.after(1000,countdown)

def nextcolor():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set() # e is entry box variable
        if e.get().lower() == colors[1].lower():
            score +=1

        e.delete(0,END)
        random.shuffle(colors)

        label.config(fg = str(colors[1]),text= str(colors[0]))
        scoreLabel.config(text = "Score: " + str(score))

instructions = Label(root,text = "Type The Color Of The Word",font=('Helvetica',12,'bold'),pady=22,bg='linen')
instructions.pack()

scoreLabel = Label(root,text = "Press Enter to start",font=('Helvetica',12,'bold'),bg='linen')
scoreLabel.pack()

timeLabel = Label(root,text = "Time Left: "+str(timeleft),font = ("Helvetica",12,'bold'),bg='linen')
timeLabel.pack()

label = Label(root,font=('times',53,'italic bold'),bg='linen',pady=8)
label.pack()

e = Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()

root.mainloop()



