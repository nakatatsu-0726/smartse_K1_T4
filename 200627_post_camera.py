import requests
import time
import picamera

url = "https://notify-api.line.me/api/notify" 
token = "トークン指定"
headers = {"Authorization" : "Bearer "+ token} 
message =  "郵便が投函されました" 

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
# Camera warm-up time
    time.sleep(2)
    camera.capture('my_picture.jpg')

    fname='my_picture.jpg'


    payload = {"message" :  message} 
    files = {"imageFile": open(fname, "rb")} 
    r = requests.post(url, headers = headers, params=payload, files=files) 