from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('chromedriver.exe')  # 크롬 드라이버가 위치한 경로 대입 필요
browser.maximize_window()  # 창 최대화

# browser = webdriver.Chrome()
# def set_chrome_driver():
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# return driver

# 네이버 항공권
url = "https://www.naver.com"
# browser = set_chrome_driver()

browser.get(url)  # url로 이동
elem = browser.find_element(By.NAME, "query")
elem.click()
elem.send_keys("네이버 항공")
elem.send_keys(Keys.ENTER)
# elem = browser.find_element(By.CLASS_NAME, "link_name")
# elem.click()

# https://www.youtube.com/watch?v=qhy8I4ChCuw(find_element 셀레니움4버전 바뀌면서 사용하는 방법)
# 가는 날 선택 클릭
browser.find_element(
    By.CLASS_NAME, "sp_flight flight_btn flight_btn_calendar").click()

# browser.find_element(By.CLASS_NAME, "sc-furvIG lkLLxz num").click() # 이번달 31일 선택

# 이번달 31일, 다음달 2일 선택
# browser.find_elements(By.LINK_TEXT, "31")[0].click() # 이번달
# browser.find_elements(By.LINK_TEXT, "11")[1].click() # 다음달

# 다음달 27, 28일 선택
# browser.find_elements(By.LINK_TEXT, "27")[1].click()
# browser.find_elements(By.LINK_TEXT, "28")[1].click()

# 도쿄 선택
# browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div/ul/li[1]/button/figure/img").click()
browser.find_element(By.CLASS_NAME, "_name").click()
browser.find_element(
    By.XPATH, "//*[@id='_flight_section']/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]/a").click()

# 항공권 검색 클릭
browser.find_element(By.CLASS_NAME, "sp_flight flight_btn_search").click()

# 로딩 처리
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[3]/div[1]/div/button")))
    # 성공했을 때 동작 처리
    print(elem.text)  # 첫번째 결과 출력
finally:
    browser.quit()
