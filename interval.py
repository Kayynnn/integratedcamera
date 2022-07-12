import random
from paho.mqtt import client as mqtt_client
from pytz import HOUR, timezone
from datetime import datetime

import subprocess

piserialnum = subprocess.check_output("cat /sys/firmware/devicetree/base/serial-number", shell=True)
piserialnum = str(piserialnum.strip()).strip("b\'")       
piserialnum = piserialnum[0:16]
print(piserialnum)

broker = 'broker.emqx.io'
port = 1883
topic = "device/"+ piserialnum
print(topic)
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
       # x = "\'" + x + "\'"
        date = datetime.now()
        tz   = timezone("Etc/GMT+7")
        date = date.replace(tzinfo=tz)
        date = str(date)
        date = date[0:19]
        print(x)
        with open('remote_conf.txt', 'w+') as f:
            f.write(x)
        with open('intervalLog.txt', 'a') as flog:
            flog.write('\nInterval : '+ x + ' Time : ' +date)   
        
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
    client.loop_forever()
    lines = 0
    

while True:
    run()
