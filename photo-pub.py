#!/usr/bin/env python
import ADC0832
import time
import paho.mqtt.client as mqtt

broker_address="192.168.43.13"
print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

def init():
	ADC0832.setup()

def loop():
	while True:
		res = ADC0832.getResult() - 80
		if res < 0:
			res = 0
		if res > 100:
			res = 100
		print 'res = %d' % res
                client.publish("test",res)
		time.sleep(2)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
