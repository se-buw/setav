#!/usr/bin/env python3

from ev3dev.ev3 import *
import paho.mqtt.client as mqtt
import time

m = LargeMotor('outB')

def on_message(client,userdata,message):
        m.run_timed(time_sp=300, speed_sp=int(message.payload.decode("utf-8")))
        print("Received message: ",int(message.payload.decode("utf-8")))

mqttBroker="mqtt.eclipseprojects.io"
client=mqtt.Client("motor_run")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("ros_mqtt")
client.on_message=on_message
time.sleep(50)
client.loop_end()


