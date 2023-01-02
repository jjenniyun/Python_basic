# 주피터 노트북으로 진행
# 2. 축
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)
# 개별 폰트 설정 plt.title('꺾은선 그래프',fontfamily)
plt.plot(x,y)
plt.xlabel('X축')
plt.ylabel('Y축')
plt.plot(x,y)
plt.xlabel('X축', color='red')
plt.ylabel('Y축', color='#00aa00')
plt.plot(x,y)
plt.xlabel('X축', color='red',loc='right') # left, center, right
plt.ylabel('Y축', color='#00aa00',loc='top') # top, center, bottom

plt.plot(x,y)
plt.xticks([1,2,3])
plt.yticks([3,6,9,12])
plt.show()