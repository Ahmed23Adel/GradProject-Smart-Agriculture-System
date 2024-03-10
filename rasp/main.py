# Import necessary libraries for communication and display use
import drivers
from time import sleep
from LcdModule.OptionAbstract import GlobalContextLcd
from LcdModule.hello import HelloPage
from KeypadModule.Keypad import *
## Joystick
import RPi.GPIO as GPIO
import ADC0834
import time

#For display
display = drivers.Lcd()
gcontext = GlobalContextLcd(display)

hello_page = HelloPage(gcontext)

gcontext.cur_page = hello_page
gcontext.show_page()
    
try:
    while True:
        readLine(L1, ["1","2","3","A"], gcontext)
        time.sleep(0.1)
        readLine(L2, ["4","5","6","B"], gcontext)
        time.sleep(0.1)
        readLine(L3, ["7","8","9","C"], gcontext)
        time.sleep(0.1)
        readLine(L4, ["*","0","#","D"], gcontext)
        time.sleep(0.1)
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
