from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Setup opitons
# option = Options()
# option.add_argument("disable-infobars")
# option.add_argument("disable-extensions")
# option.add_argument("start-maximized")
# option.add_argument('disable-gpu')
# option.add_argument('headless')

# Selenium 4.0 - load webdriver
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

url = "http://naver.com"
browser = set_chrome_driver()
# 1. 네이버 이동
browser.get(url)

# 터미널로 진행
# 셀레니움 4.3.0 버전에서는 find_element_by_class_name 속성 에러 발생(메서드 삭제됨)
# find_element_by_* 그리고 find_elements_by_* 메서드가 전부 삭제됨
# find_element라이브러리 업뎃으로 인해
#from selenium.webdriver.common.by import By 넣어주고
#browser.find_element(By.CSS_SELECTOR, 'css넣을거').click() 이런식으로 표현
#elem = browser.find_element(By.CLASS_NAME,"link_login") 클래스 표현
#참고: https://pythonblog.co.kr/coding/23/

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()

# 3. id, pw 입력
browser.find_element(By.ID,"id").send_keys("naver_id")
browser.find_element(By.ID,"pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID,"log.login").click()
time.sleep(3)

# 5. id를 새로 입력
#browser.find_element(By.ID,"id").send_keys("my_id")
browser.find_element(By.ID,"id").clear()
browser.find_element(By.ID,"id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() #브라우저 종료