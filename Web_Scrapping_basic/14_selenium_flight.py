from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_util(xpath_str):
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath_str)))


browser = webdriver.Chrome()  # 크롬 드라이버가 위치한 경로 대입 필요
browser.maximize_window()  # 창 최대화

# 네이버 항공권
url = "https://flight.naver.com/"
# browser = set_chrome_driver()

browser.get(url)  # url로 이동
# 팝업창 닫기
main = browser.window_handles
# 팝업이 있는지 체크
for i in main:
    if i != main[0]:
        browser.switch_to.window(i)
        browser.close()
browser.switch_to.window(main[0])

# 가는 날 선택 클릭
begin_date = browser.find_element(By.XPATH, '//button[text()= "가는 날"]')
begin_date.click()

# time.sleep(1) # 1초 대기
wait_util('//b[text()="31"]')  # 나올때까지 30초 대기

# 이번달 31일 선택
day31 = browser.find_elements(By.XPATH, '//b[text()="31"]')
# len(day31)
day31[0].click()

# 다음달 27일 선택
wait_util('//b[text()="27"]')
day27 = browser.find_elements(By.XPATH, '//b[text()="27"]')
day27[1].click()

# 도착지 선택
arrival = browser.find_element(By.XPATH, '//b[text()="도착"]')
arrival.click()

# 국내 선택
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

# 제주 선택
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

# 항공권 검색 클릭
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

input("종료하려면 enter키를 입력하세요")
browser.quit()
