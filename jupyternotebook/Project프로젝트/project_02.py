# 주피터 노트북으로 진행
# 2. 출생아 수 및 합계출산율
import pandas as pd
df = pd.read_excel('142801_20230103004239021_excel.xlsx', skiprows=2, nrows=2, index_col=0)
df
# 참고: https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1428

df.index
df.index.values
df.rename(index={'출생아\xa0수':'출생아 수','합계\xa0출산율':'합계 출산율'}, inplace=True)
df

df.index.values
df.loc['출생아 수']
df.iloc[0]

df = df.T # row와 column을 바꿔줌
df

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15 # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 글자가 깨지는 현상 해결

plt.plot(df.index, df['출생아 수'])
plt.plot(df.index, df['합계 출산율'])
plt.show()

fig, ax1 = plt.subplots(figsize=(10,7))
ax1.plot(df.index, df['출생아 수'], c='#ff812d') # 주황

ax2 = ax1.twinx() # x축을 공유하는 쌍둥이 axis
ax2.plot(df.index, df['합계 출산율'], c='#ffd100') # 노랑

fig, ax1 = plt.subplots(figsize=(15,5))
ax1.set_ylabel('출생아 수 (천 명)')
ax1.set_ylim(250, 700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#ff812d') # 주황

ax2 = ax1.twinx() # x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], c='#ffd100') # 노랑

fig, ax1 = plt.subplots(figsize=(15,5))
ax1.set_ylabel('출생아 수 (천 명)')
ax1.set_ylim(250, 700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#ff812d') # 주황
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val+12, val, ha='center')
    
ax2 = ax1.twinx() # x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], c='#ffd100') # 노랑

fig, ax1 = plt.subplots(figsize=(15,5))
ax1.set_ylabel('출생아 수 (천 명)')
ax1.set_ylim(250, 700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#ff812d')
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val+12, val, ha='center')
    
ax2 = ax1.twinx() # x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], c='#ffd100', marker='o', ms=10, lw=5, mec='w', mew=3)

fig, ax1 = plt.subplots(figsize=(15,5))
fig.suptitle('출생아 수 및 합계 출산율')
ax1.set_ylabel('출생아 수 (천 명)')
ax1.set_ylim(250, 700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index, df['출생아 수'], color='#1ba7f2')
for idx, val in enumerate(df['출생아 수']):
    ax1.text(idx, val, val, ha='center')
    
ax2 = ax1.twinx() # x축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (가임여성 1명당 명)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index, df['합계 출산율'], c='#ffd100', marker='o', ms=10, lw=5, mec='w', mew=3)
for idx, val in enumerate(df['합계 출산율']):
    val = round(val,3)
    ax2.text(idx, val+0.08, val, ha='center')