#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

############
#
# Use this script to visualize the PWM in the oscilloscope
#
############

LedPin = 15
 
GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
GPIO.output(LedPin, GPIO.LOW)  # Set pin to low(0V)
 
p = GPIO.PWM(LedPin, 1000)     # set Frequece to 1KHz
p.start(0)                     # Start PWM output, Duty Cycle = 0
 
try:
    while True:
        p.ChangeDutyCycle(25)      # Change duty cycle
        time.sleep(4)              # sleep for 4 secs
        p.ChangeDutyCycle(50)      # Change duty cycle
        time.sleep(4)              # sleep for 4 secs
        p.ChangeDutyCycle(75)      # Change duty cycle
        time.sleep(4)              # sleep for 4 secs
        
except KeyboardInterrupt:
    p.stop()
    GPIO.output(LedPin, GPIO.HIGH)    # turn off all leds
    GPIO.cleanup()
