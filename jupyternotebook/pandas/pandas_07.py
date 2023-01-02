# 주피터 노트북으로 진행
# 7.데이터 선택(loc) : 이름을 이용하여 원하는 row에서 원하는 col선택
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df
df.loc['1번'] # index1번에 해당하는 전체 데이터
df.loc['5번'] # index 5번에 해당하는 데이터
df.loc['1번','국어'] # index1번에 해당하는 국어 데이터
df.loc[['1번','2번'],'영어'] # index 1번, 2번에 해당하는 영어 데이터
df.loc[['1번','2번'],['영어','수학']] # index 1번, 2번에 해당하는 영어, 수학 데이터
df.loc['1번':'5번','국어':'사회'] # index 1~5번까지, 국어~사회까지 데이터