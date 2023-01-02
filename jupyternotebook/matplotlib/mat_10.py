# 주피터 노트북으로 진행
# 10.DataFrame활용
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

df = pd.read_excel('../Pandas/score.xlsx')
df

plt.plot(df['지원번호'],df['키'])
# 2개 데이터
plt.plot(df['지원번호'],df['영어'])
plt.plot(df['지원번호'],df['수학'])

plt.plot(df['지원번호'],df['영어'])
plt.plot(df['지원번호'],df['수학'])

plt.grid(axis='y', color='purple', alpha=0.4, linestyle='--', linewidth=2)