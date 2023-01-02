# 주피터 노트북으로 진행
# 12. 다중 막대 그래프
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결
df = pd.read_excel('../Pandas/score.xlsx')
df

import numpy as np
#np.arange(5)
np.arange(3,6)
arr = np.arange(5)
arr+100
arr * 3

df.shape[0] # row, column
N = df.shape[0]
N
index = np.arange(N)
index

w = 0.25
plt.bar(index-w, df['국어'])
plt.bar(index, df['영어'])
plt.bar(index+w, df['수학'])

w = 0.25
plt.bar(index-w, df['국어'], width=w)
plt.bar(index, df['영어'], width=w)
plt.bar(index+w, df['수학'], width=w)

w = 0.25
plt.bar(index-w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index+w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)

plt.figure(figsize=(10,5))
plt.title('학생별 성적')

w = 0.25
plt.bar(index-w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index+w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)
plt.xticks(index, df['이름'], rotation=60)

plt.show()