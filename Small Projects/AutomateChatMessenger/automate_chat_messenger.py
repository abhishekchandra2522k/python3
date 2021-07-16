import pyautogui
import time



text = input("Enter the text: ")

counter = 3

while counter > 0:
    time.sleep(5)
    pyautogui.typewrite(text) # write the text whereever our cursor is
    time.sleep(5)   # sleep for 5 seconds
    pyautogui.press('enter') # press the enter key
    counter = counter - 1