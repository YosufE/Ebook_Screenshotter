from gi.repository import Gdk
import time
import os
from pynput.keyboard import Key, Controller

keyboard = Controller()


time.sleep(5)


# get screen dimensions


def take_Screens(name, current_page, last_page):
    if not os.path.exists(name):
        os.makedirs(name)
    for i in range(last_page - current_page + 1):
        window = Gdk.get_default_root_window()
        x, y, width, height = window.get_geometry()
        pb = Gdk.pixbuf_get_from_window(window, x, y, width, height)
        pb.savev(name+"/page"+str(current_page+i)+".png", "png", (), ())
        print("Page Nr.:" + str(current_page+i))
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        time.sleep(2)


take_Screens("Python 3 (Kaminski, Steffan)", 1, 482)
