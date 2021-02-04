
import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    

broker_address="localhost" 

client = mqtt.Client("P1") 
client.on_message=on_message 
client.connect(broker_address) 
client.loop_start() 
client.subscribe("sensors/drone01/altitude")
client.publish("sensors/drone01/altitude","OFF")
time.sleep(4) # wait
client.loop_stop() #stop the loop
