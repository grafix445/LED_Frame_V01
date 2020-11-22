#-----------------------------------
import random
import sys
import os, os.path
import argparse
from rpi_ws281x import PixelStrip, Color
from PIL import Image, ImageSequence
import time
from Bilder import bilder_import

path = '/home/pi/Desktop/LED_Frame/Bilder/'
sys.path.append('/home/pi/Desktop/LED_Frame/Bilder/')
path_menu = '/home/pi/Desktop/LED_Frame/Menu/'

#------------------------------------

gif_select = bilder_import.gif('Select.gif', path_menu)
gif_bye = bilder_import.gif('Bye.gif', path_menu)
gif_hello = bilder_import.gif('Hello.gif', path_menu)
gif_error = bilder_import.gif('Wrong.gif', path_menu)

# LED strip configuration:
LED_COUNT = 256        # Number of LED pixels.
#LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 60  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def bild_aktivieren(strip, picture, dur):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(picture[i][0], picture[i][1], picture[i][2]))
    strip.show()
    time.sleep(dur)


def gif_aktivieren(strip, gif):
    dur = float(1.00 / gif.fps)
    for i in range(0, len(gif.frames), 1):
        bild_aktivieren(strip, gif.frames[i], dur)


def bild_single_random(strip):
    auswahl= bilder_import.gif_single_import()
    for i in range(5):
        gif_aktivieren(strip, auswahl)
       


def bild_random(strip, alle_gifs):
    zufallszahl = random.randint(0, len(alle_gifs))-1
    for i in range(5):
        gif_aktivieren(strip, bilder_import.alle_gifs[j])
                   


def shutdown(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
            


def random_starten(strip):
    while True:
        try:
            bild_single_random(strip)
        
        except KeyboardInterrupt:
            auswahl = menu_ausgeben(strip)
            if auswahl == 0:
                break


            


def menu_ausgeben(strip):

    while True: 
        gif_aktivieren(strip, gif_select)
        print ("----------------")
        print("Options:")
        print("Enter 1 for Random")
        print ("Enter 2 for Silvan")
        print("Enter 3 for Andy")
        print("Enter 4 for Dulce")
        print("Enter 5 for OldStyle")
        print("Enter 0 for quit!")
        eingabe = input("----------------" + "\n" + "Make a selection: ")
    

        if int(eingabe) == 0:
            shutdown(strip)
            gif_aktivieren(strip, gif_bye)
            print ("Program exit!")
            
            #os.system("shutdown now -h +0.1")
        
        elif int(eingabe) == 1:
            main()

        elif int(eingabe) == 2: #Silvan
            button_aktivieren("WeekendFace.gif", "Test3.mp3")
            random_starten(strip)
        
        elif int(eingabe) == 3: #Andy
            return 3
        
        elif int(eingabe) == 4: #Dulce
            return 4
        
        elif int(eingabe) == 5: #OldStyle
            button_aktivieren("OldStyle.gif", "Test3.mp3")
            random_starten(strip)

        else:
            print("Falsche Eingabe")
            gif_aktivieren(strip, gif_error)
            continue






def main():
    gif_aktivieren(strip, gif_hello)
    random_starten(strip)
    

#Main program logic:
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    #Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    #Intialize the library (must be called once before other functions).
    strip.begin()

    main()














