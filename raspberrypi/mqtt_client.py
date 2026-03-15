import paho.mqtt.client as mqtt

broker = "localhost"
topic = "hostel/room101"

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print("Data received from ESP32:")
    print(data)
    print("-----------------------")

client = mqtt.Client()

client.connect(broker,1883)

client.subscribe(topic)

client.on_message = on_message

print("Waiting for data...")

client.loop_forever()
