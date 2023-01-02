# 주피터 노트북으로 진행
# 1.인구 피라미드
# 참고 : https://jumin.mois.go.kr/ageStatMonth.do

# 남자 데이터 정의
import pandas as pd
file_name = '202212_202212_연령별인구현황_월간.xlsx'
df_m = pd.read_excel(file_name, skiprows=3, index_col='행정기관',usecols='B,E:Y')
df_m.head(3)
df_m.iloc[0] = df_m.iloc[0].str.replace(',','').astype(int) # 1,194,460 → 1194460(정수형)
df_m.iloc[0]

# 여자 데이터 정의
df_w = pd.read_excel(file_name, skiprows=3, index_col='행정기관',usecols='B,AB:AV')
df_w.head(3)
df_m.columns
df_w.columns
df_w.columns = df_m.columns # 컬럼명 통일
df_w.columns

df_w.iloc[0] = df_w.iloc[0].str.replace(',','').astype(int) # 1,194,460 → 1194460(정수형)
df_w.iloc[0]

# 데이터 시각화
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15 # 글자크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시 마이너스 글자가 깨지는 현상 해결

plt.figure(figsize=(10,7))
plt.barh(df_m.columns, -df_m.iloc[0] // 1000) # 단위 : 천명
plt.barh(df_w.columns, df_w.iloc[0] // 1000)
plt.title('2022 대한민국 인구 피라미드')
plt.savefig('2022_인구피라미드.png', dpi=100)
plt.show()