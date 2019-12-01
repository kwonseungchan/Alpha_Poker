import board
import neopixel
import time

#pixels = neopixel.NeoPixel(board.D18, 24)


class neo:

    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 24)

    def neo(self, player, bet_amount):
        self.pixels = neopixel.NeoPixel(board.D18, 24)
        self.pixels.fill ((0,0,0))

        if player == "인공지능":
            if bet_amount == 1: 
                self.pixels.fill ((0,25,0))
                time.sleep(0.9)
                 
            elif bet_amount== 2:
                self.pixels.fill ((0,25,0))
                time.sleep(1.5)
                 
            elif bet_amount== 3:
                self.pixels.fill ((0,25,0))
                time.sleep(2.0)
                 
            elif bet_amount == 4:
                self.pixels.fill ((0,25,0))
                time.sleep(2.7)
                 
            elif bet_amount == 5:
                self.pixels.fill ((0,25,0))
                time.sleep(3.35)
                 
            elif bet_amount == 6:
                self.pixels.fill ((0,25,0))
                time.sleep(3.95)
                 
            elif bet_amount == 7:
                self.pixels.fill ((0,25,0))
                time.sleep(4.6)
                 
            elif bet_amount == 8:
                self.pixels.fill ((0,25,0))
                time.sleep(5.15)
                 
            elif bet_amount == 9:
                self.pixels.fill ((0,25,0))
                time.sleep(5.7)
                 
            elif bet_amount == 10:
                self.pixels.fill ((0,25,0))
                time.sleep(6.2)
                 
            elif bet_amount == 11:
                self.pixels.fill ((0,25,0))
                time.sleep(6.85)
                 
            elif bet_amount == 12:
                self.pixels.fill ((0,25,0))
                time.sleep(7.37)
                 
            elif bet_amount == 13:
                self.pixels.fill ((0,25,0))
                time.sleep(7.97)
                    
            elif bet_amount == 14:
                self.pixels.fill ((0,25,0))
                time.sleep(8.5)
                 
            elif bet_amount == 15:
                self.pixels.fill ((0,25,0))
                time.sleep(8.96)
                 
            elif bet_amount == 16:
                self.pixels.fill ((0,25,0))
                time.sleep(9.5)
                 
            elif bet_amount == 17:
                self.pixels.fill ((0,25,0))
                time.sleep(10.1)
                 
            elif bet_amount == 18:
                self.pixels.fill ((0,25,0))
                time.sleep(10.7)
                 
            elif bet_amount == 19:
                self.pixels.fill ((0,25,0))
                time.sleep(11.2)
                 
            elif bet_amount == 20:
                self.pixels.fill ((0,25,0))
                time.sleep(11.8)
                 

        elif player == "플레이어":
                if bet_amount == 1: 
                    self.pixels.fill ((255,255,255))
                    time.sleep(1)
                     
                elif bet_amount== 2:
                    self.pixels.fill ((255,225,255))
                    time.sleep(1.8)
                     
                elif bet_amount== 3:
                    self.pixels.fill ((255,225,255))
                    time.sleep(2.5)
                     
                elif bet_amount == 4:
                    self.pixels.fill ((255,255,255))
                    time.sleep(3.1)
                     
                elif bet_amount == 5:
                    self.pixels.fill ((255,255,255))
                    time.sleep(3.8)
                     
                elif bet_amount == 6:
                    self.pixels.fill ((255,255,255))
                    time.sleep(4.5)
                     
                elif bet_amount == 7:
                    self.pixels.fill ((255,255,255))
                    time.sleep(5.2)
                     
                elif bet_amount == 8:
                    self.pixels.fill ((255,225,255))
                    time.sleep(5.9)
                     
                elif bet_amount == 9:
                    self.pixels.fill ((255,225,255))
                    time.sleep(6.6)
                     
                elif bet_amount == 10:
                    self.pixels.fill ((255,225,255))
                    time.sleep(7.2)
                     
                elif bet_amount == 11:
                    self.pixels.fill ((255,225,255))
                    time.sleep(8)
                     
                elif bet_amount == 12:
                    self.pixels.fill ((255,225,255))
                    time.sleep(8.6)
                     
                elif bet_amount == 13:
                    self.pixels.fill ((255,225,255))
                    time.sleep(9.5)
                     
                elif bet_amount == 14:
                    self.pixels.fill ((255,225,255))
                    time.sleep(10.2)
                     
                elif bet_amount == 15:
                    self.pixels.fill ((255,225,255))
                    time.sleep(10.9)
                     
                elif bet_amount == 16:
                    self.pixels.fill ((255,225,255))
                    time.sleep(11.65)
                     
                elif bet_amount == 17:
                    self.pixels.fill ((255,225,255))
                    time.sleep(12.35)
                     
                elif bet_amount == 18:
                    self.pixels.fill ((255,225,255))
                    time.sleep(12.95)
                     
                elif bet_amount == 19:
                    self.pixels.fill ((255,225,255))
                    time.sleep(13.7)
                     
                elif bet_amount == 20:
                    self.pixels.fill ((255,225,255))
                    time.sleep(14.36)
                     

        self.pixels.fill ((0,0,0))


