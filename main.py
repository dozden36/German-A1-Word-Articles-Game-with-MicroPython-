from machine import Pin, SPI
import neopixel
import random
import time
import st7735

SPI_ID = 0
sck_pin = Pin(2)
sda_pin = Pin(3)
cs_pin = Pin(1)
dc_pin = Pin(4)
res_pin = Pin(5)
blk_pin = Pin(6, Pin.OUT)
blk_pin.value(1)

btn_der = Pin(14, Pin.IN, Pin.PULL_UP)
btn_die = Pin(27, Pin.IN, Pin.PULL_UP)
btn_das = Pin(26, Pin.IN, Pin.PULL_UP)

np = neopixel.NeoPixel(Pin(16), 1)

spi = SPI(SPI_ID, baudrate=10000000, polarity=0, phase=0,
          sck=sck_pin, mosi=sda_pin)
tft = st7735.ST7735(spi, 160, 80, cs=cs_pin, dc=dc_pin, rst=res_pin, rotation=1)

BLACK = 0x0000
WHITE = 0xFFFF
RED = 0xF800
GREEN = 0x07E0
BLUE = 0x001F
YELLOW = 0xFFE0

words = [
    ("der", "Apfel"),
    ("das", "Auto"),
    ("die", "Banane"),
    ("das", "Buch"),
    ("der", "Computer"),
    ("die", "Frau"),
    ("das", "Haus"),
    ("der", "Mann"),
    ("die", "Milch"),
    ("das", "Wasser"),
    ("die", "Schule"),
    ("der", "Tisch")
]

def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

def set_led(r, g, b):

    np[0] = (g, r, b)
    np.write()

def success_animation():

    for _ in range(2):
        set_led(0, 50, 0)
        time.sleep(0.1)
        set_led(0, 0, 0)
        time.sleep(0.1)

def scary_error_animation():
    for _ in range(4):
        set_led(100, 0, 0)
        time.sleep(0.05)
        set_led(0, 0, 0)
        time.sleep(0.05)
        set_led(100, 0, 0)
        time.sleep(0.1)
        set_led(20, 0, 0)
        time.sleep(0.05)

def main():
    question_indices = list(range(len(words)))
    shuffle_list(question_indices)
    
    idx = 0
    while idx < len(question_indices):
        q_index = question_indices[idx]
        correct_article, current_word = words[q_index]
        
        draw_question(current_word, "der   die   das")
        set_led(0, 0, 0)
        
        answered_correctly = False
        
        while not answered_correctly:
            chosen = None
            if btn_der.value() == 0:
                chosen = "der"
                time.sleep(0.25)
            elif btn_die.value() == 0:
                chosen = "die"
                time.sleep(0.25)
            elif btn_das.value() == 0:
                chosen = "das"
                time.sleep(0.25)
                
            if chosen:
                if chosen == correct_article:
                    success_animation()
                    answered_correctly = True
                else:
                    scary_error_animation()
                    
            time.sleep(0.05)
            
        idx += 1
        
    tft.fill(BLACK)
    tft.text("Congrats!", 40, 30, GREEN)
    tft.show()
    set_led(0, 30, 30)

main()
