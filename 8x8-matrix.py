import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

APIN = [23,  9, 11, 12, 13, 25, 16, 20]
CPIN = [21, 24, 26, 18,  5, 19, 10,  6]

for i in APIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

for i in CPIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

SLEEP_LEN = 0.0005
r_index = 0

try:
    for col in APIN:
        GPIO.output(col, GPIO.HIGH)
    
    while True:
        GPIO.output(CPIN[r_index], GPIO.LOW)
        sleep(SLEEP_LEN)
        GPIO.output(CPIN[r_index], GPIO.HIGH)
        r_index = (r_index + 1) % 8
        
except KeyboardInterrupt:
    GPIO.cleanup()



