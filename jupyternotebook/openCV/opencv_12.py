# 주피터 노트북으로 진행
# 12 이미지 변형(원근)
# 1)사다리꼴 이미지 펼치기
import cv2
import numpy as np

img = cv2.imread('newspaper.jpg')

width, height = 640, 240 # 가로크기 640 세로크기 240 결과물 출력

src = np.array([[511,352], [1008, 345], [1122,584], [455,594]], dtype=np.float32) # input 4개 지점
dst = np.array([[0,0],[width,0],[width, height], [0,height]], dtype=np.float32) # output 4개 지점
# 좌상, 우상, 우하, 좌하(시계방향으로 4개 지점 정의)

matrix = cv2.getPerspectiveTransform(src, dst) # matrix얻어옴
result = cv2.warpPerspective(img, matrix, (width, height)) # matrix대로 변환

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2)회전된 이미지 올바로 세우기
import cv2
import numpy as np

img = cv2.imread('poker.jpg')

width, height = 530, 710

src = np.array([[702,143], [1133,414], [726,1007], [276,700]], dtype=np.float32) # input 4개 지점
dst = np.array([[0,0],[width,0],[width, height], [0,height]], dtype=np.float32) # output 4개 지점
# 좌상, 우상, 우하, 좌하(시계방향으로 4개 지점 정의)

matrix = cv2.getPerspectiveTransform(src, dst) # matrix얻어옴
result = cv2.warpPerspective(img, matrix, (width, height)) # matrix대로 변환

cv2.imshow('img',img)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 미니 프로젝트 : 반자동 문서 스캐너
