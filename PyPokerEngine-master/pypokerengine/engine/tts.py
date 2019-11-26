import os
import sys
import urllib.request
import pygame
import ssl


class tts:

    client_id = "zgcwecgcix"
    client_secret = "0uoOEq3DOde5vU6Tt27sKaL3ohuSvex7odKDRl9e"

    def requestTts(self, quote):
        ssl._create_default_https_context = ssl._create_unverified_context
        encText = urllib.parse.quote(quote)
        data = "speaker=mijin&speed=0&text=" + encText;
        url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
        request = urllib.request.Request(url)
        request.add_header("X-NCP-APIGW-API-KEY-ID",self.client_id)
        request.add_header("X-NCP-APIGW-API-KEY",self.client_secret)
        response = urllib.request.urlopen(request, data=data.encode('utf-8'))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            with open('./pypokerengine//engine/tts.mp3', 'wb') as f:
                f.write(response_body)
            print("TTS mp3 저장")
        else:
            print("Error Code:" + rescode)

    def playTts(self, quote):
        self.requestTts(self, quote)

        file = './pypokerengine//engine/tts.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.time.wait(100)
        pygame.mixer.quit