from PIL import Image
import os, os.path
from random import randint

path = '/home/pi/Desktop/LED_Frame/Bilder/'

alle_files = os.listdir(path)
alle_bilder = []




for i in range (0, len(alle_files),1):
    if ".gif" in alle_files[i]:
        alle_bilder.append(alle_files[i])


alle_gifs = []

def gif_single_import():
    number = randint(0, len(alle_bilder)) - 1
    selected_gif = gif(alle_bilder[number])
    return selected_gif

def gifs_importieren():
    for i in range(0, len(alle_files), 1):
        if ".gif" in alle_files[i]:
            alle_gifs.insert(i, gif(alle_files[i])) #Liste [gif1][gif2][gif3][gif4]


def getPixel_list(image):
    #Pixel ist eine Liste mit allen RGB-Werten als Tupel
    pixel = []
    zaehler = 0

    # i = Zeile; k=Spalte
    # Zeilen auslesen
    for i in range(0, 16, 1):

        # Zeile gerade (links --> rechts)
        if i % 2 == 0:
            for k in range(15, -1, -1):
                pixel.insert(zaehler, image.getpixel((k, i)))
                zaehler += 1

        # Zeile ungerade (rechts --> links)
        if i % 2 == 1:
            for k in range(0, 16, 1):
                pixel.insert(zaehler, image.getpixel((k, i)))
                zaehler += 1
    return pixel


def frames_konvertieren(frames):
    for i in range (len(frames)):
        img = frames[i]
        konv_img = getPixel_list(img)
        frames[i] = konv_img


class gif:
    def __init__(self, file_name, path = '/home/pi/Desktop/LED_Frame/Bilder/'):
        self.gif = Image.open(path + file_name)
        self.frames = [] #Liste [img1][img2][img3][img4][img5]
        self.description = file_name
        self.duration = self.gif.info['duration']
        self.fps = 1000/self.duration
        ct = 0
        try:
            while True:
                self.gif.seek(ct)
                self.frames.insert(ct, self.gif.convert('RGB'))
                ct = ct + 1
        except EOFError:
            pass

        frames_konvertieren(self.frames) #Liste [pxList1][pxList2][pxList3]





class image_pic:
    def __init__(self, image):
        self.pixel_list = getPixel_list(image)





def main():
    #gifs_importieren()
    gif_single_import()



main()








