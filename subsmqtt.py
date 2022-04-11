#!/usr/bin/python3
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 9999)

def on_connect(client, userdata, flags, rc):
    print ("connected to broker")
    client.subscribe("./test")

def on_message(client, userdata, message):
    print (message.payload.decode())
    print ("message recieved")

while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()