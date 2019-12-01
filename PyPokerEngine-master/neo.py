import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 24)

a = int(input("input :"))

pixels[0] = (255,0,0)
#pixels[1] = (255,0,0)
pixels.fill((0,0,0))

for i in range (a) :
    pixels.fill((0,0,0))
    time.sleep(2)
    pixels.fill((0,255,0))
   # pixels.fill((255,255,255))
    time.sleep(10)
    pixels.fill((0,0,0))

for i in range (b) :
    pixels.fill((0,0,0))
    time.sleep(2)
    pixels.fill((125,0,200))
    time.sleep(5)
    pixels.fill((0,0,0))


