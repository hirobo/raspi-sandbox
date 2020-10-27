import RPi.GPIO as GPIO
import time, sys

SWITCH = 18
LED = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

while True:
    try:
        if (GPIO.input(SWITCH) == GPIO.HIGH):
            print("high")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print("low")
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
