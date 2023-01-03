# 주피터 노트북으로 진행
# 8. 이미지 대칭
# 1)좌우 대칭
import cv2
img = cv2.imread('img.jpg')
flip_horizontal = cv2.flip(img, 1) # flipCode > 0 : 좌우대칭 horizontal

cv2.imshow('img',img)
cv2.imshow('flip_horizontal', flip_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2)상하 대칭
import cv2
img = cv2.imread('img.jpg')
flip_vertical = cv2.flip(img, 0) # flipCode == 0 : 상하대칭 vertical

cv2.imshow('img',img)
cv2.imshow('flip_vertical', flip_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3)상하좌우 대칭
import cv2
img = cv2.imread('img.jpg')
flip_both = cv2.flip(img, -1) # flipCode < 0 : 상하좌우대칭

cv2.imshow('img',img)
cv2.imshow('flip_both', flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()