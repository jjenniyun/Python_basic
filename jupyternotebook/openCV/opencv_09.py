# 주피터 노트북으로 진행
# 9. 이미지 회전
# 1)시계방향 90도 회전
import cv2
img = cv2.imread('img.jpg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도 회전

cv2.imshow('img',img)
cv2.imshow('rotate_90',rotate_90)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2)180도 회전
import cv2
img = cv2.imread('img.jpg')

rotate_180 = cv2.rotate(img, cv2.ROTATE_180) # 180도 회전

cv2.imshow('img',img)
cv2.imshow('rotate_180',rotate_180)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3)시계반대방향으로 90도 회전
import cv2
img = cv2.imread('img.jpg')

rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대방향으로 90도 회전

cv2.imshow('img',img)
cv2.imshow('rotate_270',rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows()