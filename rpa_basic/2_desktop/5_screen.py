import pyautogui
# 스크린 샷 찍기
#img = pyautogui.screenshot()
#img.save("screenshot.png") # 파일 저장

#pyautogui.mouseInfo()
pixel = pyautogui.pixel(18,19)
print(pixel)

#print(pyautogui.pixelMatchesColor(18,19, (34,167,242)))
#print(pyautogui.pixelMatchesColor(18,19, pixel))
print(pyautogui.pixelMatchesColor(18,19, (30,137,211)))


