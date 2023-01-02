# 주피터 노트북으로 진행

# 14. 원 그래프(심화)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스 글자가 깨지는 현상 해결
values = [30, 25, 20, 13, 10, 2]
labels = ['Python','Java','JavaScript','C#','C/C++','ETC']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
explode = [0.05]* 6

plt.pie(values, labels=labels, autopct='%.f%%', startangle=90, counterclock=False, colors=colors, explode=explode)
plt.show()

wedgeprops = {'width':0.6, 'edgecolor':'w', 'linewidth':2}
plt.pie(values, labels=labels, autopct='%.f%%', startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops)
plt.show()

def custom_autopct(pct):
    #return ('%.f%%' % pct) if pct >=10 else ''
    return '{:.0f}%'.format(pct) if pct >= 10 else ''

plt.pie(values, labels=labels, autopct=custom_autopct, startangle=90, counterclock=False, colors=colors, wedgeprops=wedgeprops, pctdistance=0.7)
plt.show()

# DataFrame활용
df = pd.read_excel('../Pandas/score.xlsx')
df

grp = df.groupby('학교')
grp.size()['북산고']

values=[grp.size()['북산고'], grp.size()['능남고']] # [5,3]
labels = ['북산고','능남고']

plt.pie(values, labels=labels)
plt.title('소속 학교')
plt.show()