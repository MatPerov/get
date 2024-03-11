import RPi.GPIO as GPIO
import time as t
leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)
k = 1
while k == 1: 
    for i in range(8):
        a = GPIO.input(aux[i])
        GPIO.output(leds[i], a)