# 주피터 노트북으로 진행
# 5.파일 저장
# 이미지 저장
import cv2
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = cv2.imwrite('img_save.jpg', img)
print(result)

# 저장 포맷(jpg, png)
import cv2
img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기
cv2.imwrite('img_save.png', img) # png형태로 저장

# 동영상 저장
import cv2
cap = cv2.VideoCapture('video.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 프레임크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) * 2 # 영상 재생속도가 2배

out = cv2.VideoWriter('output_fast.avi', fourcc, fps, (width, height))
# 저장 파일명, 코덱, fps, 크기 (width, height)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
        
    out.write(frame) # 영상데이터만 저장(소리x)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'):
        break
        
out.release() # 자원 해제        
cap.release()
cv2.destroyAllWindows()