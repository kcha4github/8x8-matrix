import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

APIN = [23,  9, 11, 12, 13, 25, 16, 20]
CPIN = [21, 24, 26, 18,  5, 19, 10,  6]

DISPLAY = [ 0b00011000,
            0b00100100,
            0b01000010,
            0b10000001,
            0b11111111,
            0b10000001,
            0b10000001,
            0b10000001,
            ]

CB = 50
C1 = 500
C2 = C1 - CB

HELLO_WORLD = [
    [C1,[ 0b10000001,
          0b10000001,
          0b10000001,
          0b11111111,
          0b10000001,
          0b10000001,
          0b10000001,
          0b00000000]], # H
    [C1,[ 0b00000000,
          0b00011000,
          0b00100100,
          0b01000010,
          0b01111110,
          0b01000000,
          0b00100000,
          0b00011100]], # e
    [C2,[ 0b00011000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001100]], # l
    [CB,[ 0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000]], # _
    [C2,[ 0b00011000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001100]], # l
    [C1,[ 0b00000000,
          0b00011000,
          0b00100100,
          0b01000010,
          0b01000010,
          0b00100100,
          0b00011000,
          0b00000000]], # o
    [C1,[ 0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000]], # _
    [C1,[ 0b10000001,
          0b10000001,
          0b10000001,
          0b10011001,
          0b01011010,
          0b01011010,
          0b00100100,
          0b00000000]], # W
    [C1,[ 0b00000000,
          0b00011000,
          0b00100100,
          0b01000010,
          0b01000010,
          0b00100100,
          0b00011000,
          0b00000000]], # o
    [C1,[ 0b00000000,
          0b00000000,
          0b01100110,
          0b00101000,
          0b00110000,
          0b00100000,
          0b00100000,
          0b00000000]], # r
    [C1,[ 0b00011000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001100]], # l
    [C1,[ 0b00000100,
          0b00000100,
          0b00110100,
          0b01001100,
          0b01000100,
          0b01001100,
          0b00110110,
          0b00000000]], # d
    [C1,[ 0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000]], # _
]

for i in APIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

for i in CPIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

SLEEP_LEN = 0.0005
tick = 0
str_index = 0
r_index = 0

try:
    for col in APIN:
        GPIO.output(col, GPIO.HIGH)
    
    while True:
        if tick >= HELLO_WORLD[str_index][0]:
            str_index += 1
            tick = 0
            if str_index >= len(HELLO_WORLD):
                str_index = 0

        bitmap = HELLO_WORLD[str_index][1]
        line = bitmap[r_index]
        for c_index in range(8):
            if (line & (0b10000000 >> c_index)) > 0:
                GPIO.output(APIN[c_index], GPIO.HIGH)
            else:
                GPIO.output(APIN[c_index], GPIO.LOW)
        
        GPIO.output(CPIN[r_index], GPIO.LOW)
        sleep(SLEEP_LEN)
        GPIO.output(CPIN[r_index], GPIO.HIGH)
        r_index = (r_index + 1) % 8

        tick += 1
        
except KeyboardInterrupt:
    GPIO.cleanup()



