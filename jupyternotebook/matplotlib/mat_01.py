# 주피터 노트북으로 진행
# Matplotlib : 다양한 형태의 그래프를 통해서 데이터 시각화를 할 수 있는 라이브러리
import matplotlib.pyplot as plt

# 1. 그래프 기본
x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)
print(plt.plot(x,y))
plt.plot(x,y)
plt.show()

# Title 설정
plt.plot(x,y)
plt.title('Line Graph')

# 한글 폰트 설정
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

import matplotlib.font_manager as fm
fm.fontManager.ttflist # 사용가능한 폰트 확인
[f.name for f in fm.fontManager.ttflist]

plt.plot(x,y) # 양수
plt.title('꺾은선 그래프')
plt.plot([-1,0,1],[-5,-1,2])