# 자동주문 시스템 제작 
# 조건1 1보다 작거나 숫자가 아닌 입력값이 들어올 떄 valueerror로 처리
# 출력메시지: "잘못된 값을 입력하였습니다."

# 조건2 대기손님이 주문할 수 있는 총 치킨량 10마리 한정
# 치킨 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
# 출력 메시지: "재고가 소진되어 더이상 주문을 받지 않습니다."

# [코드]

class SoldOutError(Exception):
    pass

chicken = 10
wait =1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken: #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(wait, order))
            wait += 1
            chicken -= order
            
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.")
        break