import RPi.GPIO as GPIO
import ADC0834
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(14)== GPIO.HIGH:
        print("Up pushed")
        time.sleep(1)
    if GPIO.input(15)== GPIO.HIGH:
        print("Down pushed")
        time.sleep(1)
    if GPIO.input(18)== GPIO.HIGH:
        print("center pushed")
        time.sleep(1)

