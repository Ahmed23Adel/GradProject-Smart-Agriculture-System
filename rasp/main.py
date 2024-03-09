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

##Keypad
L1 = 25
L2 = 8
L3 = 7
L4 = 1
C1 = 12
C2 = 16
C3 = 20
C4 = 21
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
        gcontext.append_char(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
        gcontext.append_char(characters[1])
    if(GPIO.input(C3) == 1):
        print(characters[2])
        gcontext.append_char(characters[2])
    if(GPIO.input(C4) == 1):
        print(characters[3])
        gcontext.append_char(characters[3])
    GPIO.output(line, GPIO.LOW)
    
    
    
try:
    while True:
        readLine(L1, ["1","2","3","A"])
        time.sleep(0.1)
        readLine(L2, ["4","5","6","B"])
        time.sleep(0.1)
        readLine(L3, ["7","8","9","C"])
        time.sleep(0.1)
        readLine(L4, ["*","0","#","D"])
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
