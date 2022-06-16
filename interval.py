import random
import os
from paho.mqtt import client as mqtt_client
import time

def getserial():
    # Extract serail from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR0000000000"
    return cpuserial    

piserialnum = getserial()
broker = 'broker.emqx.io'
port = 1883
topic = "device/" + piserialnum
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker,port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
       # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        x = msg.payload.decode()
        print(x)
        with open('interval.txt', 'w+') as f:
            f.write(x)
        
       # lines = 0
        #if os.path.isfile('interval.txt'):
         #  f = open('interval.txt')
          # lines = f.read()
     
        #print(lines)       

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    lines = 0
    

while True:
    run()
    time.sleep(2)
    # client = connect_mqtt()
    # subscribe(client)
