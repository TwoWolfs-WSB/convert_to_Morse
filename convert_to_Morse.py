#!/usr/bin/python3
from tkinter import *
import input_text as t

root = Tk()
root.title("Morse converter")

def button_click():
    text = e.get()
    e.delete(0,END)
    t.input_text(text)

e = Entry(root, width=30,borderwidth=5)
e.grid(row=0, column=0,columnspan=3,padx=10,pady=10)

button_1 = Button(root, text="Go!",padx=40,pady=20,command=button_click)
button_1.grid(column=1,row=1)
root.mainloop()


#t.input_text(text)
