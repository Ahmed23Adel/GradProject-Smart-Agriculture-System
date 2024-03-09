# Import necessary libraries for communication and display use
import drivers
from time import sleep
from LcdModule.OptionAbstract import GlobalContextLcd
from LcdModule.hello import HelloPage

display = drivers.Lcd()
gcontext = GlobalContextLcd(display)

hello_page = HelloPage(gcontext)

gcontext.cur_page = hello_page
gcontext.show_page()
# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first


# Main body of code
try:
    while True:
        gcontext.show_page()
        sleep(2)
        gcontext.clear()
        sleep(1)
        # Remember that your sentences can only be 16 characters long!
        #print("Hello from Rowling")
        #display.lcd_display_string("Hi from Rowling", 1)  # Write line of text to first line of display
        #display.lcd_display_string("Plants Magic", 2)  # Write line of text to second line of display
        #sleep(2)                                           # Give time for the message to be read
        #display.lcd_display_string("I am a display!", 1)   # Refresh the first line of display with a different message
        #sleep(2)                                           # Give time for the message to be read
        #display.lcd_clear()                                # Clear the display of any data
        #sleep(2)                                           # Give time for the message to be read
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
