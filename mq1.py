#!/usr/bin/python3
# Simple MQTT client that subscribes to a topic and prints messages
import paho.mqtt.client as mqtt

myBroker = 'XXX.XXX.XXX.XXX' # Your MQTT Server address goes here

def on_message(myClient, obj, msg):
    print('Message in topic:',msg.topic)
    print('Message:',msg.payload.decode('UTF-8'))


myClient = mqtt.Client()

# Connect to a broker
print('Connecting to:', myBroker)
myClient.connect(myBroker)

# Subscribe to kitchen lights
myClient.subscribe('house/kitchen/lights')
#myClient.subscribe('+/kitchen/+') # Uncomment to subscribe to all kitchen topics 

myClient.on_message = on_message

myClient.loop_forever()
