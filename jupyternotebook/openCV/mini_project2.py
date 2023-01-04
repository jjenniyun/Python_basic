# 주피터 노트북으로 진행
# 미니 프로젝트 : 개별 카드 추출해서 파일 저장
import cv2
img = cv2.imread('card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출

COLOR = (0,200, 0) # 녹색

idx = 1
for cnt in contours:
    if cv2.contourArea(cnt) > 25000: # 카드 한장크기: 가로*세로
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x,y), (x+width, y+height),COLOR, 2) # 사각형 그림
        
        crop = img[y:y+height, x: x+width]
        cv2.imshow(f'card_crop_{idx}', crop)
        cv2.imwrite(f'card_crop_{idx}.png',crop) # 파일 저장
        idx += 1

cv2.imshow('img',img)
cv2.imshow('contour',target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()