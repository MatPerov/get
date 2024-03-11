import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

for i in range (4):
    GPIO.output(21, 1)
    t.sleep(1)
    GPIO.output(21, 0)
    t.sleep(1)