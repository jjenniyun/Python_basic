# 주피터 노트북으로 진행
# 11. 누적막대 그래프
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

df = pd.read_excel('../Pandas/score.xlsx')
df

plt.bar(df['이름'],df['국어'])
plt.bar(df['이름'],df['영어'])

plt.bar(df['이름'],df['국어'])
plt.bar(df['이름'],df['영어'], bottom=df['국어']) # 누적 막대 그래프: 밑을 국어 데이터

plt.bar(df['이름'],df['국어'])
plt.bar(df['이름'],df['영어'], bottom=df['국어'])
plt.bar(df['이름'],df['수학'], bottom=df['국어']+df['영어'])

plt.bar(df['이름'],df['국어'], label='국어')
plt.bar(df['이름'],df['영어'], bottom=df['국어'], label='영어')
plt.bar(df['이름'],df['수학'], bottom=df['국어']+df['영어'], label='수학')

plt.xticks(rotation=45)
plt.legend()
