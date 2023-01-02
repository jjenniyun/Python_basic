# 주피터 노트북으로 진행
# 6. 데이터 선택(기본)
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# Column 선택(label)
df['이름']
df['키']
df[['이름','키']]

# Column선택(정수 Index)
df.columns
df.columns[0]
df.columns[2]
df[df.columns[0]] # 0번째 column에 해당하는 데이터 가져옴
# df['이름']과 동일한 동작
df[df.columns[-1]] # 맨 끝에 있는 값을 가져옴

# 슬라이싱
df['영어'][0:5] # 0~4까지의 영어 점수 데이터 가져옴
df[['이름','키']][:3] # 처음 3명의 이름, 키 정보를 가져옴
df[3:]