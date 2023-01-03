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

# 원
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR = (255,255,0) # 옥색
RADIUS = 50 # 반지름
THICKNESS = 10 # 두께

cv2.circle(img, (200,100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 원
# 그릴 위치, 원의 중심점, 반지름, 색깔, 두께, 선 종류
cv2.circle(img, (400,100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA) # 속이 꽉 찬 원

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 사각형
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR = (0,255,0) # 초록색
THICKNESS = 3 # 두께

cv2.rectangle(img, (100,100), (200,200), COLOR, THICKNESS) # 속이 빈 사각형
# 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
cv2.rectangle(img, (300,100), (400,200), COLOR, cv2.FILLED) # 속이꽉찬 사각형

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 다각형
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

COLOR = (0,0,255) # 빨간색
THICKNESS = 3 # 두께

pts1 = np.array([[100,100], [200,100], [100,200]])
pts2 = np.array([[200,100],[300,100],[300,200]])
#cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
#cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 리스트 형태로 넣어주면 속이 빈 다각형 형태
# 그릴 위치, 좌표, 닫힘 여부, 색깔, 두께, 선 종류

pts3 = np.array([[[100,300],[200,300],[100,400]],[[200,300],[300,300],[300,400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA) # 꽉찬 다각형
# 그릴 위치, 좌표, 색깔, 선 종류

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()