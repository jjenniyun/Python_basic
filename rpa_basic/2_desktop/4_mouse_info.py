import pyautogui
#pyautogui.FAILSAFE = False 가급적 사용하지 않는게 좋음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
#pyautogui.mouseInfo()

for i in range(5):
    pyautogui.move(100,100)