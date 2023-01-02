# 주피터 노트북으로 진행
# 15. 산점도 그래프
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

df = pd.read_excel('../Pandas/score.xlsx')
df
df['학년'] = [3,3,2,1,1,3,2,2]
df

plt.scatter(df['영어'],df['수학'])
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

import numpy as np
sizes = np.random.rand(8) * 1000
sizes

plt.scatter(df['영어'],df['수학'], s= sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

sizes = df['학년'] * 500 # 1학년 500 / 2학년 1000 / 3학년 1500
plt.scatter(df['영어'],df['수학'], s= sizes)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

plt.scatter(df['영어'],df['수학'], s= sizes, c=df['학년'], cmap='Pastel2', alpha=0.3) # 색깔을 학년별로 분류, 적용
# 참고 : https://matplotlib.org/stable/gallery/color/colormap_reference.html
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.show()

plt.figure(figsize=(10,5))
plt.scatter(df['영어'],df['수학'], s= sizes, c=df['학년'], cmap='Pastel2', alpha=0.8)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.colorbar(ticks=[1,2,3], label='학년', shrink=0.5, orientation='horizontal')
plt.show()