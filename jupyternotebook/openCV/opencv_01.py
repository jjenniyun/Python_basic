# 주피터 노트북으로 진행
# 1. 이미지 출력
# 환경설정
#Anaconda prompt에서 다음 명령 수행
#- pip install opencv-python
#- 오류 발생 시 : 참고(https://hello-bryan.tistory.com/418)

import cv2
cv2.__version__

# OpenCV(Computer Version): 다양한 영상(이미지) / 동영상 처리에 사용되는 오픈소스 라이브러: 
import cv2
img = cv2.imread('img.jpg') # 해당 경로의 파일 읽어오기
cv2.imshow('img',img) # img라는 이름의 창에 img표시
cv2.waitKey(0) # 지정된 시간(ms) 동안 사용자 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기

# 읽기 옵션
# 1. cv2.IMREAD_COLOR : 컬러이미지. 투명영역은 무시(기본값)
# 2. cv2.IMREAD_GRAYSCALE : 흑백이미지
# 3. cv2.IMREAD_UNCHANGED : 투명 영역까지 포함

import cv2
img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_unchanged', img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Shape : 이미지의 height, width, channel 정보
import cv2
img = cv2.imread('img.jpg')
img.shape # 세로, 가로, channel