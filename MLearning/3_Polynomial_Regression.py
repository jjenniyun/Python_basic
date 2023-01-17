# 주피터 노트북으로 진행
# 3. Polynomial Regression 다중 회귀
# 공부시간에 따른 시험 점수 (우등생)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('PolynomialRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# 3-1. 단순선형회귀(Simple Linear Regression)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X,y) # 전체 데이터로 학습

# 데이터 시각화(전체)
plt.scatter(X,y, color='blue') # 산점도
plt.plot(X, reg.predict(X), color='green') # 선 그래프
plt.title('Score by hours (genius)') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # y축 이름
plt.show()

reg.score(X,y) # 전체 데이터 통한 모델 평가

# 3-2. 다항회귀(Polynomial Regression)
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4) # 4차
X_poly = poly_reg.fit_transform(X)
X_poly[:5] # [x] → [x^0, x^1, x^2] → x가 3이라면 [1,3,9] 변환
X[:5] # 서로 비교, 2차원 배열

poly_reg.get_feature_names_out()

lin_reg = LinearRegression()
lin_reg.fit(X_poly,y) # 변환된 x와 y를 가지고 모델 생성(학습)

# 데이터 시각화(변환된 X와 y)
plt.scatter(X,y, color='blue') # 산점도
plt.plot(X, lin_reg.predict(poly_reg.fit_transform(X)), color='green') # 선 그래프
plt.title('Score by hours (genius)') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # y축 이름
plt.show()

X_range = np.arange(min(X),max(X),0.1) # X의 최솟값에서 최대값까지의 범위를 0.1단위로 잘라서 데이터 생성
X_range
X_range.shape
X_range[:5]

X_range = X_range.reshape(-1,1) # row개수는 자동으로 계산,  column개수는 1개
X_range.shape

plt.scatter(X,y, color='blue') # 산점도
plt.plot(X_range, lin_reg.predict(poly_reg.fit_transform(X_range)), color='green') # 선 그래프
plt.title('Score by hours (genius)') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # y축 이름
plt.show()

# 공부시간에 따른 시험 성적 예측
reg.predict([[2]]) # 2시간 공부했을 때 선형 회귀 모델의 예측
lin_reg.predict(poly_reg.fit_transform([[2]])) # 2시간 공부했을 때 다항회귀 모델의 예측
lin_reg.score(X_poly,y)