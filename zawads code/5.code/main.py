import time
from asyncore import loop
import pyautogui

pyautogui.moveTo( 820,850)  # moves mouse to X of 100, Y of 200.
pyautogui.click( button='left')

# writng the massege  

time.sleep(4)
pyautogui.write("techzawad.blogspot.com")
# sending
time.sleep(2)
pyautogui.press('enter')
