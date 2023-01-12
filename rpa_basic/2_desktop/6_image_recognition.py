import pyautogui
#file_menu = pyautogui.locateOnScreen("file_menu.png")
#print(file_menu)
#pyautogui.click(file_menu)

#plus_icon = pyautogui.locateOnScreen("plus.png")
#pyautogui.moveTo(plus_icon)

#screen = pyautogui.locateOnScreen("screenshot.png")
#print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
    # print(i)
    # pyautogui.click(i, duration=0.25)

checkbox = pyautogui.locateOnScreen("checkbox.png")
pyautogui.click(checkbox)