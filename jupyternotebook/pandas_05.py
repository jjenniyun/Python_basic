# 주피터 노트북으로 진행
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# DataFrame 확인: 계산 가능한 데이터에 대해 column별로 데이터의 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌
df.describe()
df.info()
df.head() # 처음 5개의 row를 가져옴
df.head(7) # 처음 7개의 row를 가져옴
df.tail() # 마지막 5개 row를 가져옴
df.tail(3) # 마지막 3개 row를 가져옴
df.values
df.index
df.columns
df.shape # row, column
df

# Series 확인
df['키'].describe() # 1차원 데이터 가져옴
df['키'].min()
df['키'].max()
df['키'].nlargest(3) # 키큰 사람 순서대로 3명 데이터
df['키'].mean()
df['키'].sum()
df['SW특기'].count()
df['학교'].unique() # 중복제외한 값
df['학교'].nunique()