# 50명의 승객과 매칭 기회가 있을 때 총 탑승 승객 수 구하는 프로그램 작성
# 조건1) 승객별 운행 소요 시간 5~50분 
# 조건2) 소요시간 5~15분 사이의 승객만 매칭해야함

# 출력문 예제)
# [0] 1번째 손님(소요시간: 15분)
# [ ] 3번째 손님 (소요시간 50분)
# ...
# 총 탑승 승객 : 2분

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1,51): # 1~50(승객 수)
    time = randrange(5, 51) # 5~50분 소요시간
    if 5<= time <= 15: # 5~ 15분 이내 손님(매칭 성공), 탑승 승객수 증가 처리
        print("[0] {0}번째 손님(소요시간: {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님(소요시간: {1}분)".format(i, time))
        
print("총 탑승 승객 : {0}명".format(cnt))