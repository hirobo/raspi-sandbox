import RPi.GPIO as GPIO
import time, sys

SWITCH = 18
LED = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(LED, GPIO.LOW)
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
