# 주피터 노트북으로 진행
# 7. 여러 데이터
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)

# COVID-19 백신 종류별 접종 인구
days = [1,2,3] # 1일, 2일, 3일
az = [2,4,8] # (단위: 만명) 1~3일ㄲ자ㅣ 아스트라제네카 접종인구
pf = [5,1,3] # 화이자
moder = [1,2,5] # 모더나

plt.plot(days,az)
plt.plot(days,pf)
plt.plot(days,moder)

plt.plot(days,az, label='az')
plt.plot(days,pf, label='pf', marker='o', linestyle='--')
plt.plot(days,moder, label='moder', marker='s', ls='-.')

plt.legend()

plt.plot(days,az, label='az')
plt.plot(days,pf, label='pf', marker='o', linestyle='--')
plt.plot(days,moder, label='moder', marker='s', ls='-.')

plt.legend(ncol=3) # 컬럼개수 지정
