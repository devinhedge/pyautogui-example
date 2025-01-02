import pyautogui
import time
from random import randrange, uniform

try:
    while True:
        # Create a random wiat time where a random amount of tim in seconds up to 60 seconds is added to 180 seconds
        waittime = 180 + randrange(0, 60)
        pyautogui.press('right')
        pyautogui.press('left')
        time.sleep(waittime)
        
except KeyboardInterrupt:
    print('Program stopped by user')