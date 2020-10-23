 #!/usr/bin/python3

from sense_hat import SenseHat
import json

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

sensor_dict= {
    "Humidity": humidity,
    "Pressure": pressure,
    "Temperature": temperature,
    "North": north,
    "Gyroscope": gyro,
    "Accelerometer": accel
}

with open('Sensor_out.json', "w") as f:
    json.dump(sensor_dict, f, indent=4)
    print("Done")
    f.close()
