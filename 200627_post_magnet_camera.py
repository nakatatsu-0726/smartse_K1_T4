import time
import RPi.GPIO as GPIO
import requests
import picamera
import os
 
 
#line api設定
url = "https://notify-api.line.me/api/notify" 
token = "トークン指定"
headers = {"Authorization" : "Bearer "+ token} 
message =  "郵便が投函されました"
#GPIO初期化
GPIO.setmode(GPIO.BCM)
#GPIO18pinを入力モードとし、pull up設定とします 
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
sw_status = 1
 
try:
    while True:
        sw_status = GPIO.input(18)
        if sw_status == 0:
            print("Close")
        else:
            with picamera.PiCamera() as camera:
                camera.resolution = (1024, 768)
                camera.capture('my_picture.jpg')

                fname='my_picture.jpg'
                payload = {"message" :  message} 
                files = {"imageFile": open(fname, "rb")} 
                r = requests.post(url, headers = headers, params=payload, files=files)
                os.remove("/home/pi/Desktop/my_picture.jpg")
                time.sleep(5)
                
                
except KeyboardInterrupt:
    pass
GPIO.cleanup()

