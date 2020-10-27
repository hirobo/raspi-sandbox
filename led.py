import RPi.GPIO as GPIO
import time

PNO = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PNO, GPIO.OUT)

for i in range(10):
    print("i=",i)
    GPIO.output(PNO, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(PNO, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()