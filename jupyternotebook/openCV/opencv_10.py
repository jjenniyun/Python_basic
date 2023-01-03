# 주피터 노트북으로 진행
# 10. 이미지 변형(흑백)
# 1)불러온 이미지를 흑백으로 읽음
import cv2
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2)불러온 이미지를 흑백으로 변경
import cv2
img = cv2.imread('img.jpg')

dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 색깔을 바꿔줌 cvtColor

cv2.imshow('img',img)
cv2.imshow('gray', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()