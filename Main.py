import pyautogui
import time
from PIL import Image

while True:
    #OPEN IMAGES
    fish = Image.open("fish.png")

    #VARIABLES
    x = False

    time.sleep(2)
    pyautogui.moveTo(574, 709)
    pyautogui.rightClick()
    time.sleep(0.2)
    pyautogui.moveTo(607, 711)
    pyautogui.rightClick()
    time.sleep(0.2)
    x = True

    while x == True:
        fishGood = pyautogui.locateOnScreen(fish)
        if fishGood != None:
            print(fishGood)
            pyautogui.moveTo(607, 711)
            pyautogui.rightClick()
            x = False

    pyautogui.moveTo()