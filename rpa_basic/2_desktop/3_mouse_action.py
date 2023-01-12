import pyautogui

#pyautogui.sleep(3) # 3초 대기
#print(pyautogui.position())

# pyautogui.click(64, 17, duration=1) # 1초 동안 (64,17) 좌표 이동 후 마우스 클릭
# pyautogui.click()
#pyautogui.mouseDown()
#pyautogui.mouseUp()

#pyautogui.doubleClick()
#pyautogui.click(clicks=500)

# pyautogui.moveTo(200 , 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

pyautogui.sleep(3) # 3초 대기
#pyautogui.rightClick()
#pyautogui.middleClick()

#print(pyautogui.position())
pyautogui.moveTo(826, 174)
#pyautogui.drag(100, 0, duration=0.25) # 현재 위치 기준 x100만큼, y0만큼 드래그 
pyautogui.dragTo(1514, 349, duration=0.25) # 절대 좌표 기준 x 1514, y 349 드래그

pyautogui.scroll(300) # 양수이면 위 방향, 음수이면 아래방향으로 300만큼 스크롤
