# 주피터 노트북으로 진행
# 4. 텍스트
# OpenCV에서 사용하는 글꼴 종류
# 1. cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프 글꼴
# 2. cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
# 3. cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# 4. cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
# 5. cv2.FONT_ITALIC : 기울임(이탤릭체)
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

SCALE = 1 # 크기
COLOR = (255,255,255) # 흰색
THICKNESS = 1 # 두께

cv2.putText(img, "NCT-Simplex", (20,50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
# 그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께
cv2.putText(img, "NCT-Plain", (20,150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "NCT-Script Simplex", (20,250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "NCT-Triplex", (20,350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "NCT-Italic", (20,450), cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC , SCALE, COLOR, THICKNESS)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 한글
import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

SCALE = 1 # 크기
COLOR = (255,255,255) # 흰색
THICKNESS = 1 # 두께

cv2.putText(img, "안녕", (20,50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS) # 한글이 반영 안됨
# 그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 한글 우회 방법
import cv2
import numpy as np
# PIL(python image LIbrary)
from PIL import ImageFont, ImageDraw, Image

def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos,text, font=font, fill=font_color)
    return np.array(img_pil)

img = np.zeros((480,640,3), dtype=np.uint8)

FONT_SIZE = 30
COLOR = (255,255,255) # 흰색

#cv2.putText(img, "안녕", (20,50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
# 그릴 위치, 텍스트 내용, 시작위치, 폰트 종류, 크기, 색깔, 두께
img = myPutText(img, "안녕", (20,50), FONT_SIZE, COLOR)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()