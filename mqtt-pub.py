import paho.mqtt.client as mqtt

broker_address="127.0.0.1" 

print("creating new instance")
client = mqtt.Client("pub2") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

print("Publishing message to topic: test")
client.publish("test","Hello world")

#################
## Alternatively you can send a single message without creating an instance
##print "sending now"
##mqtt.single("test","Hi from paho",hostname="192.168.1.2")
