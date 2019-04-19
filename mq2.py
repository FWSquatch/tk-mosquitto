#!/usr/bin/python3
# Simple MQTT client that publishes messages to a topic
import paho.mqtt.client as mqtt
import time

myBroker = '192.168.22.60' # Your MQTT Server address goes here
myClient = mqtt.Client()

# Connect to a broker
print('Connecting to:', myBroker)
myClient.connect(myBroker)

# Flip the light on and off 
status = 'ON'
for i in range(10):
    print('Publishing status:', status)
    myClient.publish('house/kitchen/lights', status)    
    if status == 'OFF':
        status = 'ON'
    else:
        status = 'OFF'
    time.sleep(2)

myClient.loop_stop() # Run through the program once and stop
