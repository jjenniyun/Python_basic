# 주피터 노트북으로 진행
# 3. 범례
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

x = [1,2,3]
y = [2,4,8]
plt.plot(x,y, label='무슨 데이터')
plt.legend() # 범례 지정

plt.plot(x,y, label='무슨 데이터')
plt.legend(loc='lower right') # 범례 지정
# 참고 : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

plt.plot(x,y, label='무슨 데이터')
plt.legend(loc=(0.7, 0.8)) # x축, y축(0~1사이)