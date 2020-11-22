from PIL import Image
from copy import deepcopy
from random import shuffle

dateiname = 'mushroom2'
dateiendung = '.jpg'
pic = Image.open(dateiname + dateiendung)

im_height = 16
im_width = 16

rows_up = 16
rows_down = 16
rows_left = 16
rows_right = 16
background_color = (255, 255, 255, 255)


def image_auslesen_vertical(image):
    px_list_y = []
    px_list_x = []
    for i in range (0, im_height, 1):
        for k in range (0, im_width, 1):
            px_list_x.insert(k, image.getpixel((k, i)))
        px_list_y.insert(i, deepcopy(px_list_x))
        px_list_x.clear()

    return px_list_y


def image_auslesen_horizontal(image):
    px_list_y = []
    px_list_x = []

    for i in range(0, im_width, 1):
        for k in range(0, im_height, 1):
            px_list_y.insert(k, image.getpixel((i, k)))
        px_list_x.insert(i, deepcopy(px_list_y))
        px_list_y.clear()

    return px_list_x


#Frame erstellen
def frame_erstellen_ver(px_list_y):
    new_frame = Image.new('RGB', (im_width, im_height), color=0)
    for i in range (0, im_height, 1):
        for k in range (0, im_width, 1):
           new_frame.putpixel((k, i), px_list_y[i][k])
    return new_frame


def frame_erstellen_hor(px_list_x):
    new_frame = Image.new('RGB', (im_width, im_height), color=0)
    for i in range (0, im_height, 1):
        for k in range (0, im_width, 1):
           new_frame.putpixel((i, k), px_list_x[i][k])
    return new_frame



#MOVE one row

def move_up_one_row(image):
    px_list = image_auslesen_vertical(image)

    for i in range (0, im_height-1, 1):
        px_list[i] = deepcopy(px_list[i+1])

    for k in range (0, im_width, 1):
        px_list[15][k] = background_color

    return px_list


def move_down_one_row(image):
    px_list = image_auslesen_vertical(image)

    for i in range (im_height-1, 1, -1):
        px_list[i] = deepcopy(px_list[i-1])

    for k in range (0, im_width, 1):
        px_list[0][k] = background_color

    return px_list


def move_left_one_row(image):
    px_list = image_auslesen_horizontal(image)

    for i in range(0, im_width-1, 1):
        px_list[i] = deepcopy(px_list[i + 1])

    for k in range(0, im_height, 1):
        px_list[15][k] = background_color

    return px_list

def move_right_one_row(image):
    px_list = image_auslesen_horizontal(image)

    for i in range(im_width - 1, 1, -1):
        px_list[i] = deepcopy(px_list[i - 1])

    for k in range(0, im_height, 1):
        px_list[0][k] = background_color

    return px_list


#MOVE up/down/left/right

def move_up():
    image_list_up = []
    image_list_up.insert(0, pic)
    image_list_down = []
    image_list_down.insert(0, pic)

    for i in range(0, rows_up + 1, 1):
        image_list_up.insert(i + 1, frame_erstellen_ver(move_up_one_row(image_list_up[i])))

    for k in range(0, rows_down + 1, 1):
        image_list_down.insert(k + 1, frame_erstellen_ver(move_down_one_row(image_list_down[k])))

    del image_list_up[0]


    image_list_down.reverse()
    image_list_down.extend(image_list_up)
    return image_list_down


def move_down():
    return_list = move_up()
    return_list.reverse()
    return return_list


def move_right():
    image_list_right = []
    image_list_right.insert(0, pic)
    image_list_left = []
    image_list_left.insert(0, pic)

    for i in range(0, rows_right + 1, 1):
        image_list_right.insert(i + 1, frame_erstellen_hor(move_right_one_row(image_list_right[i])))

    for k in range(0, rows_left + 1, 1):
        image_list_left.insert(k + 1, frame_erstellen_hor(move_left_one_row(image_list_left[k])))

    del image_list_right[0]

    image_list_right.reverse()
    image_list_right.extend(image_list_left)
    return image_list_right


def move_left():
    return_list = move_right()
    return_list.reverse()
    return return_list


def gif_erstellen():
    image_list = []
    image_list.insert(0, move_up())
    image_list.insert(0, move_down())
    image_list.insert(0, move_right())
    image_list.insert(0, move_left())
    shuffle(image_list)
    return image_list



def main():

    shuffled_img_list = gif_erstellen()
    new_gif = []

    for i in range (0, len(shuffled_img_list),1):
        new_gif.extend(shuffled_img_list[i])





    new_gif[0].save(dateiname + '.gif', save_all = True, append_images = new_gif[1:], duration = 100, loop = 0)

    new = Image.open(dateiname + '.gif')

    new.save(dateiname + '_.gif', save_all = True, duration = 100)






main()



