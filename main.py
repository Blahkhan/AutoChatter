import pyautogui, time
print("After 5 seconds, chat be spammed")
time.sleep(5)
f = open("Text.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
