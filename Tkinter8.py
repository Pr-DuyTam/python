from tkinter import *

from tkinter.ttk import *
window = Tk()
window.title('Lập trình Tkinter')
window.geometry('350x200')

combo = Combobox(window)

combo['value']= (1, 2, 3, 4, 5, 'Text')

combo.current(1)

combo.grid(column=0,row=0)

window.mainloop()