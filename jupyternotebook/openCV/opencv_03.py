# 주피터 노트북으로 진행
# 3. 도형 그리기
# 빈 스케치북 만들기
import cv2
import numpy as np

# 세로 480 * 가로 640, 3 channel(RGB)에 해당하는 스케치북 만들기
img = np.zeros((480,640,3), dtype=np.uint8)
#img[:] = (255,255,255) # 전체 공간을 흰색으로 채우기(BGR)
#print(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 일부영역 색칠
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)
img[100:200, 200:300] = (255,255,255)
# [세로영역, 가로영역]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 직선
#직선의 종류(line type)

# 1. cv2.LINE_4 : 상하좌우 4방향으로 연결된 선
# 2. cv2.LINE_8 : 대각선을 포함한 8방향으로 연결된 선(기본값)
# 3. cv2.LINE_AA : 부드러운 선(anti-aliasing)
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR = (0,255,255) # BGR : YELLOW , 색깔
THICKNESS = 3 # 두께

cv2.line(img, (50,100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50,200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50,300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)
# 그릴 위치, 시작점, 끝 점, 색깔, 두께, 선종류

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()