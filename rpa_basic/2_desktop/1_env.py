import pyautogui # 오류 시 새로운cmd창을 열어서 pip install pyautogui 설치하기

size = pyautogui.size() # 현재 화면의 스크린 사이즈 가져옴
print(size) # 가로, 세로 크기 알 수 있음
# size[0] : width
# size[1] : height