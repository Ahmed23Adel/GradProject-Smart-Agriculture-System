# Import necessary libraries for communication and display use
import drivers
from time import sleep
from LcdModule.OptionAbstract import GlobalContextLcd
from LcdModule.hello import HelloPage

## Joystick
import RPi.GPIO as GPIO
import ADC0834
import time


display = drivers.Lcd()
gcontext = GlobalContextLcd(display)

hello_page = HelloPage(gcontext)

gcontext.cur_page = hello_page
gcontext.show_page()
# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first

##buttons
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
gcontext.show_page()
try:
    while True:
        if GPIO.input(14)== GPIO.HIGH:
            print("Up pushed")
            gcontext.move_up()
            time.sleep(.5)
        if GPIO.input(23)== GPIO.HIGH:
            print("Down pushed")
            gcontext.move_down()
            time.sleep(.5)
        if GPIO.input(18)== GPIO.HIGH:
            print("center pushed")
            gcontext.perform_action()
            time.sleep(1)
        
        #sleep(2)
        #gcontext.clear()
        #sleep(1)
        
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
