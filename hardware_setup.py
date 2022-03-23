# Pushbuttons are wired between the pin and Gnd
# Pico pin  Meaning
# ESP.IO16 Up
# ESP.IO17 Left
# ESP.IO34 Right
# ESP.IO32 Down
# ESP.IO36 Center


from machine import TouchPad, Pin, SPI, freq
import gc

from drivers.st7789.st7789_4bit import *
SSD = ST7789

spi = SPI(2, baudrate=40000000, polarity=1)
gc.collect()  # Precaution before instantiating framebuf
pcs = Pin(5, Pin.OUT)
pdc = Pin(33, Pin.OUT)
prst = Pin(32, Pin.OUT)
ssd = SSD(spi, height=240, width=240, cs=pcs, dc=pdc, rst=prst)

from gui.core.ugui import Display, quiet
# quiet()
# Create and export a Display instance

# # Define control buttons
prv = TouchPad(Pin(27))  # P0 - BIG, Touch7
sel = TouchPad(Pin(14))  # P1 - Big, Touch6
nxt = TouchPad(Pin(13))  # P2 - BIG, Touch4

disp = Display(ssd, nxt, sel, prv)
