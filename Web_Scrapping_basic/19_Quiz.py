# 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램 만들기
# 조회조건
# 1) http://daum.net 접속
# 2) '송파 헬리오시티' 검색
# 3) 다음 부동산 부분에 나오는 결과 정보

# 출력결과
# 매물1
# 거래: 매매 / 면적: 84/59(공급/전용) / 가격: 165,000(만원) / 동:214동 / 층: 고/23
# 주의사항
# 위 매물이 없을 시 다른 곳 대체 가능

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#with open("quiz.html", "w", encoding="utf-8", ) as f:
    #f.write(soup.prettify())
    
# data = soup.find("div",attrs={"class":"css-1dbjc4n r-14lw9ot r-13awgt0 r-1mlwlqe r-eqz5dr"}).find("")
# for index,row in enumerate(data):
    # columns = row.find_all()
    
    # print("{============= 매물 {} ===============}".format(index+1))
    # print("거래 :")
    # print("매물 :")
    # print("가격 :")
    # print("동 :")
    # print("층 :")