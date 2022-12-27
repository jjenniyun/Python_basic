# 사용자 정의 에러
class BigNumError(Exception):
    def __init__(self,msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

# 예외 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번쨰 숫자를 입력하세요 : "))
    num2 = int(input("첫번쨰 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumError("입력값 : {0}, {1}".format(num1, num2)) # 일부러 에러 발생시켜서 
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: # 실행되지 않고 에러 구문 출력
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력해주세요")
except BigNumError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력해주세요")
    print(err)
finally: # 무조건 출력: 에러가 발생하던지 간에 출력
    print("계산기를 이용해주셔서 감사합니다.")