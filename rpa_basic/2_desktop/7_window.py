import pyautogui

# fw = pyautogui.getActiveWindow() #현재 활성화 된 창(vscode)
# print(fw.title) # 창의 제목정보
# print(fw.size) # 창의 크기 정보(width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left+25, fw.top+20)
# 
# for w in pyautogui.getAllWindows():
    # print(w) # 모든 윈도우 가져오기 

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate # 활성화(맨앞으로 가져오기)

if w.isMaximized == False:
    w.maximize() # 최대화
    
# if w.isMinimized == False:
    # w.minimize() # 최소화
    
w.restore() # 화면 원본

w.close() # 윈도우 닫기