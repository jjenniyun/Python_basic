# 주피터 노트북으로 진행
# 5. 파일저장
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)

plt.savefig('graph.png', dpi=100)
plt.figure(dpi=200)
plt.plot(x,y)
plt.savefig('gragh_200.png', dpi=100)