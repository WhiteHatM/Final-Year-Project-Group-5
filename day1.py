import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
time.sleep(2)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

while True:
    i=GPIO.input(11)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected")
        camera.capture("/home/pi/Pictures/Img {0}.jpg".format{current_time})
        time.sleep(2)
