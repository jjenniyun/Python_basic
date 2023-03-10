# 주피터 노트북으로 진행
# 미니 프로젝트 : 반자동 문서 스캐너
# 마우스 이벤트 등록
import cv2

def mouse_handler(event, x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽버튼 클릭
        print("왼쪽 버튼 down")
        print(x,y)
    elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼 뗌
        print("왼쪽 버튼 up")
        print(x,y)
    elif event == cv2.EVENT_LBUTTONDBLCLK: # 마우스 왼쪽버튼 더블클릭
        print("왼쪽 버튼 double click")
    #elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
        #print("마우스 이동")
    elif event == cv2.EVENT_RBUTTONDOWN: # 오른쪽 버튼 클릭
        print("오른쪽 버튼 down")
    
img = cv2.imread('poker.jpg')
cv2.namedWindow('img') # img란 이름의 윈도우를 먼저 만들어 두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 프로젝트
import cv2
import numpy as np

point_list = []
src_img = cv2.imread('poker.jpg')

COLOR = (255, 0 , 255) # 핑크
THICKNESS = 2
drawing = False # 선 그릴지 여부

def mouse_handler(event, x,y,flags, param):
    global drawing
    dst_img = src_img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽버튼 클릭
        drawing = True # 선 그리기 시작
        point_list.append((x,y))
        
    if drawing:
        prev_point = None # 직선의 시작점
        for point in point_list:
            cv2.circle(dst_img, point, 5, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
        
        next_point = (x,y) # 마지막 점에서도 선 표시
        if len(point_list) == 4:
            show_result() # 결과 출력
            next_point = point_list[0] # 첫번째 클릭한 지점
            
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
        
    cv2.imshow('img',dst_img)
    
def show_result():
    width, height = 530, 710
    src = np.float32(point_list)
    dst = np.array([[0,0],[width,0],[width, height], [0,height]], dtype=np.float32) # output 4개 지점
    # 좌상, 우상, 우하, 좌하(시계방향으로 4개 지점 정의)

    matrix = cv2.getPerspectiveTransform(src, dst) # matrix얻어옴
    result = cv2.warpPerspective(src_img, matrix, (width, height)) # matrix대로 변환
    cv2.imshow('result', result)

cv2.namedWindow('img') # img란 이름의 윈도우를 먼저 만들어 두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()