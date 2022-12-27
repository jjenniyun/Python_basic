# 1명은 치킨, 3명은 커피쿠폰 추첨 프로그램 작성

# 조건1 편의상 댓글은 20명이 작성, 아이디 1~20 가정
# 조건2 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 random모듈의 shuffle 과 sample 활용

# 출력예제
# -- 당첨자 발표 --
# 치킨 당첨자: 1/ 커피 당첨자: [2,3,4] ---축하합니다---

# 활용예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # 무작위로 순서 변경
# print(lst)
# print(sample(lst,1)) # sample 무작위로 1개 뽑음

from random import *
users = range(1,21) # 1~20까지 숫자 생성
#print(type(users))
users= list(users)
#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명중에서 1명 치킨 3명 커피쿠폰
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0])) 
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다!! -- ")