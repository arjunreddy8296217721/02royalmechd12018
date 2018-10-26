import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin,GPIO.IN)
#counter=0
def cam():
    os.system("fswebcam -F 3 --fps 30 -r 1280*720 /home/pi/amir.jpg")
time.sleep(10)
while True:
    if GPIO.input(pirPin):
        print("Motion Detected")
        cam()
        time.sleep(5)
        #counter = counter + 1
    print("nothing")
    time.sleep(2)
exit()
     
