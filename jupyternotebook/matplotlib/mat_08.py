# 주피터 노트북으로 진행
# 8.막대 그래프(기본)
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결

labels = ['이재욱','황민현','신승호'] # 이름
values=[190,180,187] # 키

plt.bar(labels, values)

labels = ['이재욱','황민현','신승호'] # 이름
values=[190,180,187] # 키
colors=['r','g','b']

plt.bar(labels, values, color=colors, alpha=0.5)

labels = ['이재욱','황민현','신승호'] # 이름
values=[190,180,187] # 키

plt.bar(labels, values)
plt.ylim(175,195)
plt.bar(labels, values, width=0.5) # bar두께 조절

plt.bar(labels, values, width=0.3)
plt.xticks(rotation=45) # x축의 이름 데이터 각도를 45로 설정
plt.yticks(rotation=45) # y축의 키 데이터 각도를 45도로 설정

labels = ['이재욱','황민현','신승호'] # 이름
values=[190,180,187] # 키
ticks=['1번학생','2번학생','3번학생']

plt.bar(labels, values)
plt.xticks(labels, ticks, rotation=90)