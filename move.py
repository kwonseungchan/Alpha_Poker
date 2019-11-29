from ev3dev.dev import *
import time

count = 0

c1 = ColorSensor()

c1.mode = 'COL-REFLECT'

mB = LargeMotor('outB')
mC = LargeMotor('outC')

while count <= 9 :
    if c1.value() < 50 :
        mB.run_forever(speed_sp = 450)
        mC.run_forever(speed_sp = 450)
    else:
        mB.stop(stop_action = 'brake')
        mC.stop(stop_action = 'brake')
        time.sleep(1000)
        count += 1



