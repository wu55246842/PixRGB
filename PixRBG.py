import win32api
import win32con
from ctypes import *
import time
import random
from PIL import ImageGrab

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def grab(x1, y1, x2, y2):
    im = ImageGrab.grab((x1, y1, x2, y2))
    return im

def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)

def get_static_mouse_point():
    last = get_mouse_point()
    while True:
        time.sleep(0.5)
        current = get_mouse_point()
        if last == current:
            return current
        last = current

def get_role_color_Output(im):
    pix = im.load()
    width = im.size[0]
    height = im.size[1]

    for y in range(height):
        for x in range(width):
            r, g, b = pix[x, y]
            print("%s %s %s" % (r,g,b))
            #with open("H:\\MyProject\\Python\\magenta-master\\test\\test.txt","a") as f:
            #    f.write("%s %s %s" % (r,g,b))
            #    f.write("\n")
    return 0

if __name__ == '__main__':
    print("Mouse moves to the bottom Center")
    time.sleep(5)
    bottomCenter = get_static_mouse_point()
    print("OK")
    time.sleep(0.5)
    offset=10
    img= grab(bottomCenter[0]-offset, bottomCenter[1]-offset, bottomCenter[0]+offset, bottomCenter[1]+offset)
    get_role_color_Output(img)
