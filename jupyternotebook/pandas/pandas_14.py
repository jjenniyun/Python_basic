# 주피터 노트북으로 진행
# 14.그룹화 : 동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df.groupby('학교')
df.groupby('학교').get_group('북산고')
df.groupby('학교').get_group('능남고')
df.groupby('학교').mean() # 계산 가능한 데이터들의 평균값
df.groupby('학교').size() # 각 그룹의 크기
df.groupby('학교').size()['능남고'] # 학교로 그룹화를 한 뒤에 능남고에 해당하는 데이터의 수
df.groupby('학교')['키'].mean() # 학교를 그룹화 한 뒤 키 평균 데이터
df.groupby('학교')[['국어','영어','수학']].mean() # 학교 그룹화: 국어 영어 수학 평균 데이터
df['학년'] =[3,3,2,1,1,3,2,2] # 학년 column 추가
df
df.groupby(['학교','학년']).mean() # 학교별, 학년별 평균 데이터
df.groupby('학년').mean() # 학년별 평균 데이터

df.groupby('학년').mean().sort_values('키')
df.groupby('학년').mean().sort_values('키', ascending=False) # 내림차순
df.groupby(['학교','학년']).sum()
df.groupby('학교')[['이름','SW특기']].count() # 학교 그룹화 : 각 학교별 sw특기 데이터 수 가져옴
school = df.groupby('학교')
school['학년'].value_counts() # 학교 그룹화: 학년별 학생 수
school['학년'].value_counts().loc['북산고'] # 북산고 학년 별 학생수
school['학년'].value_counts().loc['능남고'] # 능남고 학년별 학생수
school['학년'].value_counts(normalize=True).loc['북산고'] # 학생들의 수 데이터를 퍼센트로 비교하여 가져옴