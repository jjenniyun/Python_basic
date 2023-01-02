# 주피터 노트북으로 진행

# 16. 여러 그래프
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

df = pd.read_excel('../Pandas/score.xlsx')
df

fig, axs = plt.subplots(2,2, figsize=(15,10)) # 2*2 에 해당하는 plot들을 생성
fig.suptitle('여러 그래프 넣기')

# 첫번쨰 그래프
axs[0,0].bar(df['이름'],df['국어'],label='국어점수') # 데이터 설정
axs[0,0].set_title('첫 번째 그래프') # 제목
axs[0,0].legend() # 범례
axs[0,0].set(xlabel='이름',ylabel='점수') # x,y축 label
axs[0,0].set_facecolor('lightyellow') # 전면 색
axs[0,0].grid(linestyle='--', linewidth=0.5)

# 두번쨰 그래프
axs[0,1].plot(df['이름'],df['수학'], label='수학')
axs[0,1].plot(df['이름'],df['영어'], label='영어')
axs[0,1].legend()

# 세번쨰 그래프
axs[1,0].barh(df['이름'],df['키'])

# 네번쨰 그래프
axs[1,1].plot(df['이름'],df['사회'], color='g', alpha=0.5)
