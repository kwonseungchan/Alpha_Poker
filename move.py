
from ev3dev.dev import *
from goto import goto, comefrom, label
import time

count = 0

c1 = ColorSensor()

c1.mode = 'COL-REFLECT'

mB = LargeMotor('outB')
mC = LargeMotor('outC')

label .start

while True:
    if c1.value() < 50 :
        mB.run_forever(speed_sp = 450)
        mC.run_forever(speed_sp = 450)
    else:
        mB.stop(stop_action = 'brake')
        mC.stop(stop_action = 'brake')
        time.sleep(1000)
        goto .start
        count += 1
    if count == 9:
        break

mB.stop(stop_action = 'brake')
mC.stop(stop_action = 'brake')

