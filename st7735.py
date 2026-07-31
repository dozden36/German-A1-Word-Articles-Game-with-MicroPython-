import time
from machine import Pin, SPI
import framebuf

class ST7735(framebuf.FrameBuffer):
    def __init__(self, spi, width, height, cs, dc, rst, rotation=0):
        self.spi = spi
        self.width = width
        self.height = height
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.rotation = rotation
        
        self.cs.init(Pin.OUT, value=1)
        self.dc.init(Pin.OUT, value=0)
        self.rst.init(Pin.OUT, value=1)
        
        self.buffer = bytearray(self.width * self.height * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        
        self.reset()
        self.init_display()

    def write_cmd(self, cmd):
        self.cs(0)
        self.dc(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(0)
        self.dc(1)
        self.spi.write(buf)
        self.cs(1)

    def reset(self):
        self.rst(0)
        time.sleep_ms(50)
        self.rst(1)
        time.sleep_ms(50)

    def init_display(self):
        self.write_cmd(0x01)  # SWRESET
        time.sleep_ms(150)
        self.write_cmd(0x11)  # SLPOUT
        time.sleep_ms(255)
        
        self.write_cmd(0xB1)
        self.write_data(bytearray([0x01, 0x2C, 0x2D]))
        self.write_cmd(0xB2)
        self.write_data(bytearray([0x01, 0x2C, 0x2D]))
        self.write_cmd(0xB3)
        self.write_data(bytearray([0x01, 0x2C, 0x2D, 0x01, 0x2C, 0x2D]))
        
        self.write_cmd(0xB4)
        self.write_data(bytearray([0x07]))
        self.write_cmd(0xC0)
        self.write_data(bytearray([0xA2, 0x02, 0x84]))
        self.write_cmd(0xC1)
        self.write_data(bytearray([0xC5]))
        self.write_cmd(0xC2)
        self.write_data(bytearray([0x0A, 0x00]))
        self.write_cmd(0xC3)
        self.write_data(bytearray([0x8A, 0x2A]))
        self.write_cmd(0xC5)
        self.write_data(bytearray([0x0E]))
        
        self.write_cmd(0x21)
        
        self.write_cmd(0x36)  
        self.write_data(bytearray([0xA0 if self.rotation else 0x00]))
        
        self.write_cmd(0x3A)
        self.write_data(bytearray([0x05]))
        self.write_cmd(0x29)
        time.sleep_ms(100)

    def show(self):
        x_offset = 1
        y_offset = 26
        
        self.write_cmd(0x2A)
        self.write_data(bytearray([0x00, x_offset, 0x00, x_offset + self.width - 1]))
        self.write_cmd(0x2B)
        self.write_data(bytearray([0x00, y_offset, 0x00, y_offset + self.height - 1]))
        self.write_cmd(0x2C)
        self.write_data(self.buffer)
