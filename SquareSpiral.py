import pyautogui
import time
time.sleep(3)
distance = 200
while distance > 0:
    pyautogui.dragRelative(distance, 0, button="left")
    distance = distance - 10
    pyautogui.dragRelative(0, distance, button="left")
    pyautogui.dragRelative(-distance, 0, button="left")
    distance = distance - 10
    pyautogui.dragRelative(0, -distance, button="left")
   
