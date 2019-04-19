#!/usr/bin/python3
# Program that combines Tkinter with mqtt
import paho.mqtt.client as mqtt
from tkinter import *
import time

myBroker = '192.168.22.60' # Your MQTT Server address goes here

def on_message(myClient, obj, msg):
    person, _ , topicNum = msg.topic.split('/') # split it up into usable objects (we don't need the 'tk' which is why there is a _ there)
    payload = str(msg.payload.decode('UTF-8')) # Turn the object into readable text
    #print ("Machine:", topMach, " Type:", topType)
    if person == 'fred' and topicNum == 'topic1':
        topic1.config(text=payload)
    if person == 'john' and topicNum == 'topic1':
        topic2.config(text=payload)
    if person == 'carol' and topicNum == 'topic1':
        topic3.config(text=payload)
    
myClient = mqtt.Client() # Create my client object
myClient.on_message = on_message # Set up the on_message function

# Connect to the broker
myClient.connect(myBroker, 1883)
myClient.subscribe("+/tk/+", 0)  # Subscribe to tk topics from everyone

# Tkinter stuff
rootWindow = Tk() # Create the window
rootWindow.title('Cool Kids Status Monitor') # Set the title
rootWindow.option_add("*Font", ("Times",32,)) # Set the default font face and size

# Row 1
topic1Label = Label(rootWindow, text="Fred's status:")
topic1Label.grid(sticky = N, row = 10, column = 10)
topic1 = Label(rootWindow, text='---')
topic1.grid(sticky = N, row = 10, column = 20)

# Row 2
topic2Label = Label(rootWindow, text="John's status:")
topic2Label.grid(sticky = N, row = 20, column = 10)
topic2 = Label(rootWindow, text='---')
topic2.grid(sticky = N, row = 20, column = 20)

# Row 3
topic3Label = Label(rootWindow, text="Carol's status:")
topic3Label.grid(sticky = N, row = 30, column = 10)
topic3 = Label(rootWindow, text='---')
topic3.grid(sticky = N, row = 30, column = 20)

# Start the MQTT client and open the window
myClient.loop_start() # Don't use loop_forever() as it blocks the tk window loop
rootWindow.mainloop()