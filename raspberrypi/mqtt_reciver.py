import paho.mqtt.client as mqtt
import json
import requests
import time

url = "https://script.google.com/macros/s/AKfycbxUBIdCFvIIHn899c1IO3nlyOQmEumuHPGgf2Znsk3naqOiidHUFnCGP40u6xyOra-R/exec"

latest_data = None
no_motion = False

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("hostel/room101")

def on_message(client, userdata, msg):
    print("MQTT message received:",
    msg.payload.decode())
    global latest_data
    global no_motion

    data = json.loads(msg.payload.decode())

    motion = int(data["motion"])

    if motion == 0:
        latest_data = data
        no_motion = True
    else:
        no_motion = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost",1883,60)

client.loop_start()

while True:

    if no_motion and latest_data is not None:

        try:
            response = requests.post(url, json=latest_data)
            print("Sent to Google Sheet:", latest_data)
        except:
            print("Error sending data:",e)
    time.sleep(1)
