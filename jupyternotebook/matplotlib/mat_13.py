# 주피터 노트북으로 진행
# 13.원그래프(기본)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

values = [30, 25, 20, 13, 10, 2]
labels = ['Python','Java','JavaScript','C#','C/C++','ETC']

plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()

values = [30, 25, 20, 13, 10, 2]
labels = ['Python','Java','JavaScript','C#','C/C++','ETC']
#explode = [0.2,0.1,0,0,0,0]
explode = [0.05]*6

plt.pie(values, labels=labels, explode=explode)
plt.show()
plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1.2,0.3))
plt.show()

plt.pie(values, labels=labels, explode=explode)
plt.title('언어별 선호도')
plt.legend(loc=(1.2,0.3), title='언어')
plt.show()
