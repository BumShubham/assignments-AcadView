#Q1

import tkinter
from tkinter import *
tk = tkinter.Tk()
lbl = Label(tk, text = "Hello World")
lbl.pack()
bt1 = Button(tk, text = "Exit", width = 25, command = tk.destroy)
bt1.pack()
tk.mainloop()

#Q2

import tkinter
from tkinter import *
def write():
    lbl = Label(tk, text = "You are exiting!").pack()
tk = tkinter.Tk()
lbl = Label(tk, text = "Hello World")
lbl.pack()
bt = Button(tk, text = "Exit", width = 25, command = write)
bt.pack()
tk.mainloop()

#Q3

import tkinter
from tkinter import *
def click():
    lbl.config(text = "Ok Bye!")
tk = tkinter.Tk()
frame = Frame(tk)
frame.pack()
lbl = Label(tk,text ="Welcome")
lbl.pack()
bt1 = Button(tk, text = "Exit", width = 30, command = tk.destroy)
bt1.pack()
bt2 = Button(tk, text = "Click here to change the label", width = 40, command = click)
bt2.pack()
tk.mainloop()

#Q4

import tkinter
from tkinter import *
def write():
    print(a.get())
    print(b.get())
tk = tkinter.Tk()
lbl = Label(tk, text = "Welcome to the login page")
lbl.pack()
lbl1 = Label(tk, text = "First Name")
lbl1.pack()
a = Entry(tk)
a.pack()
lbl2 = Label(tk, text = "Last Name")
lbl2.pack()
b = Entry(tk)
b.pack()
bt1 = Button(tk, text = "Print", width = 25, command = write)
bt1.pack()
bt2 = Button(tk, text = "Exit", width = 25, command = tk.destroy)
bt2.pack()
tk.mainloop()