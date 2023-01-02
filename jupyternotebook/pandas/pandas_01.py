# 주피터 노트북으로 사용(환경)
# Pandas : 파이썬에서 사용하는 데이터 분석 라이브러리
# 1. Series - 1차원 데이터 (정수, 실수, 문자열 등)
# Series 객체 생성 : 예) 1월부터 4월까지 평균 온도 데이터(-20, -10, 10, 20)
import pandas as pd
# Series 객체 생성
# 예) 1월부터 4월까지 평균 온도 데이터(-20, -10, 10, 20)
temp = pd.Series([-20, -10, 10, 20])
print(temp)
temp[0]  # 1월 온도
temp[2]  # 3월 온도

# Series 객체 생성(Index 지정)
temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
temp['Jan']  # index jan에 해당하는 데이터 출력
temp['Apr']  # index apr에 해당하는 데이터 출력
