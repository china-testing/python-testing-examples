# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

broker_address="localhost" 

client = mqtt.Client("P1") 
client.connect(broker_address) 
client.publish("house/main-light","OFF") 