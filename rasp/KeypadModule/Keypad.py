import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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


def readLine(line, characters, gcontext):
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
    
    