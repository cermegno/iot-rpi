#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

# initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN)

broker_address="192.168.1.100"
print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

def checkdist():
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(16, GPIO.LOW)
        while not GPIO.input(18):
                pass
        t1 = time.time()
        while GPIO.input(18):
                pass
        t2 = time.time()
        return (t2-t1)*340/2


def loop():
	while True:
            d = checkdist()
            df = "%0.2f" %d
            print 'Distance: ' + df
            client.publish("piper123",df)
            time.sleep(1)

if __name__ == '__main__':

	try:
		loop()
	except KeyboardInterrupt: 
                GPIO.cleanup()
		print 'The end !'
