import RPi.GPIO as GPIO
import time, sys

SWITCH = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH, GPIO.IN)

while True:
    try:
        value = "HIGH" if GPIO.input(SWITCH) == GPIO.HIGH else "LOW"
        print(value)
        time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
