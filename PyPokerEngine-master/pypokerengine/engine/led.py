#coding: utf-8

import RPi.GPIO as GPIO
import time


class led:

    def __init__(self):
        self.GPIO
        self.GPIO.setmode(GPIO.BOARD)


    def led(self, player, bet_amount):
        GPIO.setmode(GPIO.BOARD)
        #self.LED = 11
        #self.LED2 = 8
        GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
        

        if player == "인공지능":
            if bet_amount == 1: 
                GPIO.output(11, GPIO.HIGH)   
                time.sleep(0.9)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount== 2:
                GPIO.output(11, GPIO.HIGH) 
                
                time.sleep(1.5)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount== 3:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(2.0)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount == 4:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(2.7)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount == 5:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(3.35)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount == 6:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(3.95)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount == 7:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(4.6)
                GPIO.output(11, GPIO.LOW) 
                 
            elif bet_amount == 8:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(5.15)
                GPIO.output(11, GPIO.LOW) 
            elif bet_amount == 9:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(5.7)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 10:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(6.2)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 11:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(6.85)
                GPIO.output(11, GPIO.LOW)
                 
            elif bet_amount == 12:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(7.37)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 13:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(7.97)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 14:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(8.5)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 15:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(8.96)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 16:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(9.5)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 17:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(10.1)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 18:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(10.7)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 19:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(11.2)
                GPIO.output(11, GPIO.LOW)
            elif bet_amount == 20:
                GPIO.output(11, GPIO.HIGH) 
                time.sleep(11.8)
                GPIO.output(11, GPIO.LOW)

        elif player == "플레이어":
                if bet_amount == 1: 
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(1)
                    GPIO.output(8, GPIO.LOW)
                     
                elif bet_amount== 2:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(1.8)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount== 3:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(2.5)
                    GPIO.output(8, GPIO.LOW) 
                elif bet_amount == 4:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(3.1)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 5:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(3.8)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 6:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(4.5)
                    GPIO.output(8, GPIO.LOW) 
                elif bet_amount == 7:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(5.2)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 8:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(5.9)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 9:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(6.6)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 10:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(7.2)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 11:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(8)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 12:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(8.6)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 13:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(9.5)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 14:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(10.2)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 15:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(10.9)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 16:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(11.65)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 17:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(12.35)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 18:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(12.95)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 19:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(13.7)
                    GPIO.output(8, GPIO.LOW)
                elif bet_amount == 20:
                    GPIO.output(8, GPIO.HIGH) 
                    time.sleep(14.36)
                    GPIO.output(8, GPIO.LOW)

        GPIO.cleanup()


