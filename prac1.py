#!/usr/bin/python3
"""
Readjust this Docstring as follows:
Names: Khaya Mxenge
Student Number: MXNKHA002
Prac: Prac 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from time import sleep
from itertools import product
#values
counter=0
LED_display =[0,0,0]

#initialize
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#cleanup
GPIO.cleanup()
print("cleanup complete")

#set LEDs
GPIO.setup(7,GPIO.OUT) #set pin 7 to be output and set to low
GPIO.setup(11,GPIO.OUT) #set pin 11
GPIO.setup(15,GPIO.OUT) #set pin 15
LEDs=(7,11,15)
print("LEDs set")
 
def setBUTTON(pin):
    GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#convert to bi
comb = list(product([1,0],repeat=3))
display=comb[::-1]

#define functions

def DecToBi():
    global counter

    GPIO.output(LEDs,display[counter]) 

def UP(channel):
    global counter
    counter+=1
    DecToBi()

def DOWN(channel):
    global counter
    counter-=1
    DecToBi()

#set buttons
setBUTTON(29)
GPIO.add_event_detect(29,GPIO.RISING,callback=UP,bouncetime=300)
setBUTTON(33)
GPIO.add_event_detect(33,GPIO.RISING,callback=DOWN,bouncetime=300)
print("callback and buttons set")

#start
GPIO.output(7,1)
print("test one light")
GPIO.output(LEDs,GPIO.HIGH)
print("light on")
sleep(2)
GPIO.output(LEDs,0)
GPIO.output(7,0)

print("ready to push buttons")
print("fuction of OUTPUT pins",GPIO.gpio_function(7))

# Logic that you write
def main():
    print("write your logic here")
    print(counter)
    print(LED_display)
    sleep(2)
    #end of main 


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
           main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
