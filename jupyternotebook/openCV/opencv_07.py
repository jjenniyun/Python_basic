# 주피터 노트북으로 진행
# 7. 이미지 자르기
# 동영상에도 동일하게 적용 가능
# 1)영역을 잘라서 새로운 윈도우(창)에 표시
import cv2
img = cv2.imread('img.jpg')
#img.shape : (391, 640, 3)

crop = img[100:200, 200:400] # 세로기준 100:200까지 / 가로기준 200:400까지 자름
cv2.imshow('img', img) # 원본이미지
cv2.imshow('crop', crop) # 잘린 이미지
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2)영역을 잘라서 기존 윈도우에 표시
import cv2
img = cv2.imread('img.jpg')

crop = img[100:200, 200:400] # 세로기준 100:200까지 / 가로기준 200:400까지 자름
img[100:200, 400:600] = crop

cv2.imshow('img', img) # 원본이미지
cv2.waitKey(0)
cv2.destroyAllWindows()