import pyautogui
import time

INTERVAL = 60  # you can change it

while True:
    # press 'f15' button to prevent sleep, it doesn't exist so you work won't be interrupted
    pyautogui.press('f15')
    print('running')
    time.sleep(INTERVAL)
