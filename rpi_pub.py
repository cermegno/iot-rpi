import paho.mqtt.client as mqtt

## This is the IP address of your laptop. Gets redirected with port forwarding
broker_address="192.168.43.13"
print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

print("Publishing message to topic 'test'")
client.publish("test","Greetings from Paho-mqtt in Pi")

#################
## Alternatively you can send a single message without creating an instance
##print "sending now"
##mqtt.single("test","Hi from paho",hostname="192.168.1.2")
