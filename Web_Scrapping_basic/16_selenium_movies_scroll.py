# # 구글 무비
# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     "Accept-Language": "ko-KR,ko"}
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class": "VfPpkd-EScbFb-JIbuQc UVEnyf"})
# print(len(movies))

# # with open("movie.html", "w", encoding="utf-8") as f:
# # f.write(soup.prettify()) # html문서를 예쁘게 출력

# for movie in movies:
#     title = movie.find("div", attrs={"class": "Epkrse"}).get_text()
#     print(title)

import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920*1080

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2  # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
pre_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    cur_height = browser.execute_script("return document.body.scrollHeight")
    if cur_height == pre_height:
        break

    pre_height = cur_height

print("스크롤 완료")
