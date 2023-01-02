# 주피터 노트북으로 진행
# 12.데이터 수정
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# Column수정
df['학교'].replace({'북산고':'매산고','능남고':'한림예고'})
df['학교'].replace({'북산고':'매산고'}, inplace=True)
df
df['SW특기'].str.lower()
df['SW특기'] = df['SW특기'].str.lower()
df
df['SW특기'] = df['SW특기'].str.upper()
df
df['학교'] = df['학교']+'등학교' # 학교 데이터+'등학교'
df

# column 추가
df['총합'] = df['국어']+df['영어']+df['수학']+df['과학']+df['사회']
df
df['결과'] = 'Fail' # 결과column추가하고 전체 데이터는 fail로 초기화
df
df.loc[df['총합']>400, '결과'] = 'Pass' #총합이 400보다 큰 데이터에 대해서 결과를 pass로 업데이트
df

# Column삭제
df.drop(columns=['총합']) # 총합 column 삭제
df.drop(columns=['국어','영어','수학']) # 국어 영어 수학 column삭제

# Row삭제
df.drop(index='4번') # 4번 학생 데이터 row를 삭제
filt = df['수학']<80 # 수학 80점 미만 학생 필터링
df[filt]
df[filt].index
df.drop(index=df[filt].index)

# Row추가
df.loc['9번'] = ['황민현','해남고등학교',184,90,90,90,90,90,'Kotlin',450, 'Pass'] # 새로운 row 추가
df

# Cell 수정
df.loc['4번','SW특기'] = 'Python' # 4번 학생의 sw특기 python변경
df
df.loc['5번',['학교','SW특기']] = ['능남고등학교','C'] # 5번학생 학교 능남고, sw특기 c로 변경
df

# column순서 변경
cols = list(df.columns)
cols
df= df[[cols[-1]]+cols[:-1]] # 맨 뒤에 있는 결과 column을 앞으로 가져오고, 나머지 column들과 합쳐서 순서 변경
df

# column 이름 변경
df.columns
df.columns = ['Result','Name','School','키', '국어', '영어', '수학', '과학', '사회', 'SW특기', '총합']
df