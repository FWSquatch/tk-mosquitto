#!/usr/bin/python3
# Simple tkinter program that shows off some features
from tkinter import *
import time
import random


def getRand(): # Change the text of label1 to random number
    k = random.randint(100,999)
    label1.config(text=k)

j = 0 # global counter variable
def countUp(): # Change the text of label2 by incrementing by one
    global j
    j += 1
    label2.config(text=j)

def toggle(): # Toggle the button text and color
    if button3['text'] == 'ON':
        button3.config(text='OFF', bg = 'red')
    else:
        button3.config(text='ON', bg = 'green')


rootWindow = Tk() # Make a window
rootWindow.title('My Tkinter GUI')
rootWindow.option_add("*Font", ("Helvetica",32,)) # set the default font and size for the app

# Row 1
button1 = Button(rootWindow, text='Random', command=getRand) 
button1.grid(sticky = N, row = 10, column = 10)
label1 = Label(rootWindow, text='---')
label1.grid(sticky = N, row = 10, column = 20)

# Row 2
button2 = Button(rootWindow, text='CountUP', command=countUp)
button2.grid(sticky = N, row = 20, column = 10)
label2 = Label(rootWindow, text='---')
label2.grid(sticky = N, row = 20, column = 20)

# Row 3
button3 = Button(rootWindow, text="PUSH ME", command=toggle)
button3.grid(sticky = NSEW, row = 30, column = 10, columnspan = 20) # place button, stretch it to fill its container and span it across the columns

#rootWindow.geometry("600x200") # Use this to set a fixed window size
rootWindow.mainloop() # Run the program