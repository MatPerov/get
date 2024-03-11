import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
if GPIO.input(25) == 1:
    GPIO.output(24,1)
else: 
    GPIO.output(24,0)