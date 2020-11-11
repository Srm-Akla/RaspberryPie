import paho.mqtt.client as paho
import json
from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
pressure = sense.get_pressure()
temperature = sense.get_temperature()

sense.set_imu_config(True, False, False)
north = sense.get_compass()
sense.set_imu_config(False,True, False)
gyro = sense.get_gyroscope()
sense.set_imu_config(False, False, True)
accel = sense.get_accelerometer()

broker="localhost"
port=1883

#with open("Sensor_out.json", "r") as read_file:
#    data = json.load(read_file)

#print(data)


def on_publish(client,userdata,result):
    print("data published \n")
    pass

client1= paho.Client("control1")
client1.on_publish = on_publish
#client1.will_set("sensors/pressure", payload="Offline", qos=1, retain=True)
client1.connect(broker,port)
ret= client1.publish("sensors/humidity",humidity, qos=1, retain=True)
ret= client1.publish("sensors/pressure",pressure, qos=1, retain=True)
ret= client1.publish("sensors/temperature",temperature, qos=1, retain=True)
ret= client1.publish("sensors/compass",north, qos=1, retain=True)
ret= client1.publish("sensors/gyroscope",gyro["yaw"], qos=1, retain=True)
ret= client1.publish("sensors/accelerometer",accel["yaw"], qos=1, retain=True)
