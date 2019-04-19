#!/usr/bin/python3
# Simple tkinter program that shows off some features
from tkinter import *
import paho.mqtt.client as mqtt

myBroker = 'XXX.XXX.XXX.XXX' # Your MQTT Server address goes here
myClient = mqtt.Client()

def toggleStatus():
    k = label1['text']
    if k == '  OPEN  ':
        k = 'CLOSED'
        label1.config(bg='red')
    else:
        k = '  OPEN  '
        label1.config(bg='green')
    myClient.publish('home/door1',k)
    label1.config(text=k)


myClient.connect(myBroker)

rootWindow = Tk() # Make a window
rootWindow.title('Mosquitto GUI')
rootWindow.option_add("*Font", ("Times",32,)) # set the default font and size for the app

# Row 1
button1 = Button(rootWindow, text='Front Door', command=toggleStatus) 
button1.grid(sticky = NSEW, row = 10, column = 10)
label1 = Label(rootWindow, width=20, text='---')
label1.grid(sticky = NSEW, row = 10, column = 20)

print(label1['text'])
rootWindow.geometry("600x200") # Use this to set a fixed window size
rootWindow.mainloop() # Run the program