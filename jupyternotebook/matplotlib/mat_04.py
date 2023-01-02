# 주피터 노트북으로 진행
# 4.스타일
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

x = [1,2,3]
y = [2,4,8]
plt.plot(x,y)
plt.plot(x,y, linewidth=5)

# 마커 스타일
plt.plot(x,y, marker='o')
plt.plot(x,y, marker='o', linestyle='None') # 선은 없어지고 점만 남음
plt.plot(x,y, marker='v', markersize=10)
plt.plot(x,y, marker='X', markersize=10)
# 참고: https://matplotlib.org/stable/api/markers_api.html

plt.plot(x,y, marker='o', markersize=20, markeredgecolor='red') # marker외곽선의 색깔이 바뀜
plt.plot(x,y, marker='o', markersize=20, markeredgecolor='red', markerfacecolor='yellow') 

# 선 스타일
plt.plot(x,y, linestyle=':')
plt.plot(x,y, linestyle='--')
plt.plot(x,y, linestyle='-.')
# 참고 : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

plt.plot(x,y, linestyle='-')

# 색깔
plt.plot(x,y, color='pink')
plt.plot(x,y, color='#ff0000')
plt.plot(x,y, color='b')
plt.plot(x,y, color='hotpink')
# 참고 : https://matplotlib.org/stable/gallery/color/named_colors.html

# 포맷
plt.plot(x,y, 'ro--') # ro : color, marker / -- : linestyle
plt.plot(x,y, 'bv:')
plt.plot(x,y, 'go') # linestyle이 없으므로 선이 안나옴 linestyle='None' 스타일과 동일하게 작용

# 축약어
plt.plot(x,y, marker='o', mfc='red',ms=10,mec='blue', ls=':')
# 참고 : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# 투명도
plt.plot(x,y, marker='o', mfc='red', ms=10, alpha=0.3) # alpha: 투명도(0~1)

# 그래프 크기
plt.figure(figsize=(5,10))
plt.plot(x,y)
plt.figure(figsize=(10,5), dpi=50) # dots per inch : 확대
plt.plot(x,y)

# 배경색
plt.figure(facecolor='yellow')
plt.plot(x,y)
plt.figure(facecolor='#9da5e3')
plt.plot(x,y)