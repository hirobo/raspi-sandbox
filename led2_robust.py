import RPi.GPIO as GPIO
import time, sys

ports = [4, 17]
n = len(ports)

GPIO.setmode(GPIO.BCM)

for port in ports:
    GPIO.setup(port, GPIO.OUT)
    GPIO.setup(port, GPIO.OUT)

def led_on(port_num):
    for i, port in enumerate(ports):
        value = GPIO.HIGH if port_num == i else GPIO.LOW
        GPIO.output(port, value)

while True:
    try:
        for i in range(n):
            led_on(i)
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
