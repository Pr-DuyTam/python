from tkinter import *

parent = Tk()

redbutton = Button(parent, text='Red', fg='red')
redbutton.pack(side=LEFT)
redbutton = Button(parent, text='Black', fg='black')
redbutton.pack(side=RIGHT)
redbutton = Button(parent, text='Blue', fg='blue')
redbutton.pack(side=TOP)
redbutton = Button(parent, text='Green', fg='green')
redbutton.pack(side=BOTTOM)
parent.mainloop()