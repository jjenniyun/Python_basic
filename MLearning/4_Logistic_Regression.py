# 주피터 노트북으로 진행
# 4.Logistic Regression 로지스틱 회귀
# 공부시간에 따른 자격증 시험 합격 가능성
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('LogisticRegressionData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 학습(로지스틱 회귀 모델)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# 6시간 공부했을 때 예측?
classifier.predict([[6]]) 
# 결과 1은 합격예측, 0은 불합격 예측
classifier.predict_proba([[6]]) # 합격할 확률 출력
# 불합격 확률 14%, 합격할 확률 86%

# 4시간 공부했을 때 예측?
classifier.predict([[4]])
# 결과 0 ; 불합격 예측
classifier.predict_proba([[4]]) # 합격확률 출력
# 불합격확률 62%, 합격확률 38%

# 분류 결과 예측 (테스트 세트)
y_pred = classifier.predict(X_test)
y_pred # 예측 값
y_test # 실제 값(테스트 세트)
X_test # 공부 시간(테스트 세트)

classifier.score(X_test, y_test) # 모델 평가
# 전체 테스트 세트 4개 중에서 분류 예측을 올바로 맞힌 개수 3개 → 3/4 = 0.75

# 데이터 시각화(훈련 세트)
X_range = np.arange(min(X), max(X), 0.1) # X의 최소값에서 최대값까지를 0.1단위로 잘라서 데이터 생성
X_range

p = 1 / (1+ np.exp(-(classifier.coef_*X_range + classifier.intercept_))) # y = mx+b
p
p.shape
X_range.shape
p = p.reshape(-1) # 1차원 배열 형태로 변경 p.reshape(len(p))도 가능
p.shape

plt.scatter(X_train,y_train, color='blue') # 산점도
plt.plot(X_range, p, color='green') # 선 그래프
plt.plot(X_range, np.full(len(X_range),0.5), color='red') # X_range 개수만큼 0.5로 가득찬 배열 만들기
plt.title('Probability by hours')
plt.xlabel('hours')
plt.ylabel('P')
plt.show()

# 데이터 시각화(테스트 세트)
plt.scatter(X_test,y_test, color='blue')
plt.plot(X_range, p, color='green') 
plt.plot(X_range, np.full(len(X_range),0.5), color='red') # X_range 개수만큼 0.5로 가득찬 배열 만들기
plt.title('Probability by hours (test)')
plt.xlabel('hours')
plt.ylabel('P')
plt.show()

classifier.predict_proba([[4.5]]) # 4.5시간 공부했을 때 확률(모델에서는 51% 합격 예측, 실제로는 불합격)

# 혼동 행렬(Confusion Matrix)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm

# TRUE NEGATIVE(TN)  FALSE POSITIVE(FP)
# 불합격 (예측)   합격(예측)
# 불합격 (실제)   불합격(실제)

# FALSE NEGATIVE(FN)  TRUE POSITIVE(TP)
# 불합격(예측)    합격(예측)
# 합격 (실제)     합격(실제)