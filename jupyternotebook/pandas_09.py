# 주피터 노트북으로 진행
# 9. 데이터 선택(조건) :조건에 해당하는 데이터 선택
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df['키'] >= 185 # 학생들의 키가 185이상인지 여부를 True/False
filt = (df['키']>=185)
df[filt]
df[~filt] # filt를 역으로 적용(185미만인 학생들)
df[df['키']>=185]
df.loc[df['키']>=185, '수학'] # 키가 185이상인 학생들의 수학 데이터
df.loc[df['키']>=185, ['이름','수학','과학']] # 키가 185이상인 학생들의 이름, 수학, 과학 데이터

# 다양한 조건    
# & 그리고
df.loc[(df['키']>=185) & (df['학교'] == '북산고')] # 키가 185이상인 북산고 학생 데이터
# | 또는
df.loc[(df['키']<170)| (df['키']>=200)] # 키가 170보다 작거나 200이상인 학생 데이터

# str함수
filt = df['이름'].str.startswith('송') # '송'씨 성을 가진 사람
df[filt]
filt = df['이름'].str.contains('태') # 이름에 '태'가 들어가는 사람
df[filt]
df[~filt] # 이름에 '태'가 들어가는 사람을 제외
langs = ['Python','Java']
filt = df['SW특기'].isin(langs)
df[filt]
df
langs = ['python','java']
filt = df['SW특기'].str.lower().isin(langs)
df[filt]
filt = df['SW특기'].str.contains('Java')
df[filt]
df['SW특기'].str.lower().isin(langs)
df['SW특기'].str.contains('Java', na=True) # NaN 데이터에 대해서 true로 설정
df['SW특기'].str.contains('Java', na=False) # NaN 데이터에 대해서 true로 설정
filt = df['SW특기'].str.contains('Java', na=False) # java를 포함하는 데이터 출력
df[filt]