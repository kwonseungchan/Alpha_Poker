# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import csv
from pypokerengine.engine.tts import tts

class qrReader:
        cardList = []

        def _init__(self):
            self.cardList = []

        def readQR(self, num):
                ap = argparse.ArgumentParser()
                ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
                        help="path to output CSV file containing barcodes")
                args = vars(ap.parse_args())

                print("[INFO] starting video stream...")
                vs = VideoStream(src=0).start()
 
                csv = open(args["output"], "a")
                found = set()


                        
                        
                frame = vs.read()
                frame = imutils.resize(frame, width=400)
                
                        
                barcodes = pyzbar.decode(frame)
                        
                for barcode in barcodes:
                                
                        (x, y, w, h) = barcode.rect
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                        
                                
                        barcodeData = barcode.data.decode("utf-8")
                        barcodeType = barcode.type
                
                        
                        text = "{} ({})".format(barcodeData, barcodeType)
                        cv2.putText(frame, text, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
                        
                                
                        if barcodeData not in found:
                                csv.write("{}\n".format(barcodeData))
                                csv.flush()
                                found.add(barcodeData)


                cv2.imshow("Barcode Scanner", frame)
                key = cv2.waitKey(1) & 0xFF
                
                cv2.waitKey(2000)
                        

                print("[INFO] cleaning up...")
                csv.close()
                cv2.destroyAllWindows()
                vs.stop()

                        
        def csvClean(self):
                ap = argparse.ArgumentParser()
                ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
                        help="path to output CSV file containing barcodes")
                args = vars(ap.parse_args())

                csv = open(args["output"], "w")
                csv.close()


        def returnCardList(self):
                self.csvClean(self)

                for i in range(9):
                        quote = ( str(i+1) + "번째 카드를 입력시켜주세요.")
                        tts.playTts(tts, quote)
                        time.sleep(2)
                        check = self.checkCSV(self, i)
                        while check == 0:
                            self.readQR(self, i) 
                            check = self.checkCSV(self, i)
                            if check == 0:
                                tts.playTts(tts, "다시 입력시켜주세요.")

                f = open('barcodes.csv', 'r')
                reader = csv.reader(f)
                for row in reader:
                     self.cardList.append(row)
                f.close()

                return self.cardList

        def checkCSV(self, num):
                checkList = ["", "", "", "", "", "", "", "", ""]
                count = 0

                f = open('barcodes.csv', 'r')
                reader = csv.reader(f)
                for row in reader:
                    checkList[count] = row
                    count += 1
                f.close
                    
                print(checkList)

                if checkList[num] == "":
                    return 0
                
                return 1


        
