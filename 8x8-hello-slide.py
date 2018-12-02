import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

APIN = [23,  9, 11, 12, 13, 25, 16, 20]
CPIN = [21, 24, 26, 18,  5, 19, 10,  6]

DISPLAY_STRING = "HelloWorld "
DICT = {
    'H':[ 0b10000001,
          0b10000001,
          0b10000001,
          0b11111111,
          0b10000001,
          0b10000001,
          0b10000001,
          0b00000000], # H
    'e':[ 0b00000000,
          0b00000000,
          0b00111100,
          0b01000010,
          0b01111110,
          0b01000000,
          0b00111100,
          0b00000000], # e
    'l':[ 0b00011000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001000,
          0b00001100], # l
    'o':[ 0b00000000,
          0b00011000,
          0b00100100,
          0b01000010,
          0b01000010,
          0b00100100,
          0b00011000,
          0b00000000], # o
    ' ':[ 0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000,
          0b00000000], # _
    'W':[ 0b10000001,
          0b10000001,
          0b10000001,
          0b10011001,
          0b01011010,
          0b01011010,
          0b00100100,
          0b00000000], # W
    'r':[ 0b00000000,
          0b00000000,
          0b01100110,
          0b00101000,
          0b00110000,
          0b00100000,
          0b00100000,
          0b00000000], # r
    'd':[ 0b00000100,
          0b00000100,
          0b00110100,
          0b01001100,
          0b01000100,
          0b01001100,
          0b00110110,
          0b00000000], # d
}

def init_pins(pins, value):
    for i in pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, value)

init_pins(APIN, GPIO.LOW)
init_pins(CPIN, GPIO.HIGH)

SLEEP_LEN = 0.0003
SLIDE_COUNT = 200

buf = [[],[],[],[],[],[],[],[]]
buf_width = 0

try:
    # Initialize
    for c in DISPLAY_STRING:
        if c in DICT:
            bitmap = DICT[c]
            buf_width += 8

            for r_index in range(8):
                line = bitmap[r_index]
                
                for c_index in range(8):
                    if (line & (0b10000000 >> c_index)) > 0:
                        buf[r_index].append(True)
                    else:
                        buf[r_index].append(False)

    # writing
    tick = 0
    col_start = 0
    while True:
        if tick >= SLIDE_COUNT:
            col_start += 1
            tick = 0
            if col_start >= buf_width:
                col_start = 0

        line = buf[r_index]
        for c_count in range(8):
            if line[(col_start + c_count) % buf_width]:
                GPIO.output(APIN[c_count], GPIO.HIGH)
            else:
                GPIO.output(APIN[c_count], GPIO.LOW)
        
        GPIO.output(CPIN[r_index], GPIO.LOW)
        sleep(SLEEP_LEN)
        GPIO.output(CPIN[r_index], GPIO.HIGH)
        r_index = (r_index + 1) % 8

        tick += 1
        
except KeyboardInterrupt:
    GPIO.cleanup()



