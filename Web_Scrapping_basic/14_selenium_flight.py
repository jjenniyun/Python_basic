from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

url = "https://flight.naver.com"
browser = set_chrome_driver()
browser.maximize_window() #창 최대화
browser.get(url) # url로 이동

# 가는 날 이동
browser.find_element(By.CLASS_NAME,"tabContent_option__2y4c6 select_Date__1aF7Y").click()

# 다음달 27, 28일 선택
browser.find_element(By.CLASS_NAME,"sc-evZas dDVwEk num")[0].click() # [1] → 다음달
browser.find_element(By.CLASS_NAME,"sc-evZas dDVwEk num")[0].click() # [1] → 다음달