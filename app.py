import pyautogui
import time

pyautogui.press("win")

pyautogui.write("brave")


pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("Ctrl", "Shift", "N")

pyautogui.write("imdb.com")

pyautogui.press("enter")

time.sleep(2)

pyautogui.press("tab")

pyautogui.press("tab")

pyautogui.press("tab")

pyautogui.press("tab")

pyautogui.write("there will be blood")

time.sleep(2)

pyautogui.keyDown("down")

pyautogui.press("enter")
