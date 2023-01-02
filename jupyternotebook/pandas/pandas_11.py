# 주피터 노트북으로 진행
# 11.데이터 정렬
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df.sort_values('키') # 키 기준으로 오름차순 정렬
df.sort_values('키', ascending=False) # 키 기준으로 내림차순 정렬
df.sort_values(['수학','영어'], ascending=False) # 수학, 영어 점수 기준으로 내림차순
df.sort_values(['수학','영어']) # 수학, 영어 점수 기준으로 오름차순
df.sort_values(['수학','영어'], ascending=[True, False]) # 수학 오름차순, 영어 내림차순으로 정렬
df['키'].sort_values(ascending=False)
df.sort_index(ascending=False)