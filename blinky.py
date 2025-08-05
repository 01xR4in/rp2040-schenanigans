import machine
import neopixel
import time

# From documentation, LED is connected on GPIO16, count = 1 LED
np = neopixel.NeoPixel(machine.Pin(16), 1)

while True:
    np[0] = (255, 0, 0)   # red
    np.write()
    time.sleep(0.5)
    np[0] = (255, 128, 0)   # orange
    np.write()
    time.sleep(0.5)
    np[0] = (0, 255, 0)   # green
    np.write()
    time.sleep(0.5)
    np[0] = (0, 0, 0)       # off
    np.write()
    time.sleep(0.5)