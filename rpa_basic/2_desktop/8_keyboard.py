import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("jehyun love", interval=0.25) # 한글처리는 안됨

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 2번 오른쪽 1번 l a 순서대로 적고 enter
# 참고 : https://automatetheboringstuff.com/2e/chapter20/ - keyboard attribute내용 확인

# 특수문자
# shift 4 → $
# pyautogui.keyDown("shift") # shift키를 누른 상태에서
# pyautogui.press("4") # 숫자 4 입력
# pyautogui.keyUp("shift") # shift 키 뗌

# 조합 키(Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # ctrl+a

# 간편한 조합키
# pyautogui.hotkey("ctrl","alt","shift","a") # 순서대로 눌렀다가 역순서대로 뗌
# pyautogui.hotkey("ctrl","a")

import pyperclip
# pyperclip.copy("재현사랑해") # 재현사랑해 라는 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v") # 클립보드의 내용 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("재현사랑해")

# 자동화 프로그램 종료
# window : ctrl+alt+del