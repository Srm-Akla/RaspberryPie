import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    client.subscribe("sensors/temperature")
    client.subscribe("sensors/pressure")
    client.subscribe("sensors/humidity")
    client.subscribe("sensors/compass")
    client.subscribe("sensors/gyroscope")
    client.subscribe("sensors/accelerometer")

def on_message(client, userdata, msg):
    print(msg.topic+"  =>  "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.will_set("sensors/temperature", payload="offile", qos=1, retain=True)
client.will_set("sensors/pressure", payload="offile", qos=1, retain=True)
client.will_set("sensors/humidity", payload="offile", qos=1, retain=True)
client.will_set("sensors/comapass", payload="offile", qos=1, retain=True)
client.connect("localhost", 1883, 60)
client.loop_forever()
