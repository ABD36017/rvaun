import RPi.GPIO as GPIO
import time
def cam():
    import os
    os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/Desktop/4.jpg")
    print(" pic taken")


GPIO.setmode(GPIO.BCM)

pirPin=4
GPIO.setup(pirPin,GPIO.IN)
counter=1
time.sleep(4)

while True:
    if GPIO.input(pirPin):
        print("Motion Detected")
        cam()
        time.sleep(1)
        counter=counter+1

    else:
        print("Testing")
