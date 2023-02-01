# 퀴즈 팩토리얼 구하는 재귀함수 작성
# 팩토리얼 : 주어진 수보다 작거나 같은 모든 양의 정수의 곱
# n! = n* (n-1) * (n-2 ) * ... * 1
# n! = N * (n-1)! 과 같다
# 4! = 4* (4-1)!과 같다
# 1! = 0! = 1

# 재귀함수 이해
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

result = factorial(4)
print(result) # 24