# pico_i2c_lcd.py
from lcd_api import LcdApi
from machine import I2C
import time

class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        super().__init__(num_lines, num_columns)

    def putstr(self, string):
        print(string)

    def clear(self):
        print("LCD Cleared")

    def move_to(self, col, row):
        pass