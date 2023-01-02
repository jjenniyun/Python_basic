# 주피터 노트북으로 진행
# 10.결측치 : 비어 있는 데이터
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# 데이터 채우기 fillna
df.fillna('') # NaN데이터를 빈칸으로 채움
df.fillna('없음')

import numpy as np
df['학교'] = np.nan # 학교 데이터 전체를 NaN으로 채움
df
df.fillna('모름', inplace=True)

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df
df['SW특기'].fillna('확인 중', inplace=True) # sw특기 데이터 중에서 nan에 대해서 채움
df

# 데이터 제외하기 dropna
df = pd.read_excel('score.xlsx', index_col='지원번호')
df
df.dropna(inplace=True) # 전체 데이터 중에서 NaN을 포함하는 데이터 삭제
df
df = pd.read_excel('score.xlsx', index_col='지원번호')
df
df.dropna(axis='index', how='any') # NaN가 하나라도 있는 row 삭제
df.dropna(axis='columns')
df['학교'] = np.nan
df
df.dropna(axis='columns', how='all') # 데이터 전체가 NaN인 경우에만 column삭제