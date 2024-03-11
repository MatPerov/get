import RPi.GPIO as GPIO
import time as t
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 1, 0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
t.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()


x = [2, 255, 127, 64, 32, 5, 0, 256]
y = [296, 3250, 1670, 868, 458, 112, 48, 1686]
plt.scatter(x, y)
plt.show()