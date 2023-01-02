# 주피터 노트북으로 진행
# 9.막대그래프(심화)
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

labels = ['이재욱','황민현','신승호'] # 이름
values=[190,182,187] # 키

plt.barh(labels, values) # 가로 누운 그래프
plt.xlim(175, 195)

bar = plt.bar(labels, values)
bar[0].set_hatch('/') # ////
bar[1].set_hatch('x') # xxxx
bar[2].set_hatch('||') # ....

# 참고: https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html

bar = plt.bar(labels, values)
plt.ylim(175,195)

for idx, rect in enumerate(bar):
    plt.text(idx, rect.get_height()+0.5, values[idx], ha='center', color='blue')
