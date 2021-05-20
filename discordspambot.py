import pyautogui
import webbrowser
import time

message = input("what text do you want to spam")
repeats = int(input("how often should the text be spamed?"))
delay = int(input("how much delay you want to have"))

isLoaded = input("press enter when you discord is loaded")


print ("you have 5 second before the spammy spamt")
time.sleep (5)
for i in range (0,repeats):
    if message !="":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press ("enter")
    time.sleep(delay/1000)

print("Done\n")
