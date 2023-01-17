# quiz) selenium 이용하여 업무 자동화 프로그램
# 1. w3schools 홈페이지 접속
# 2. 화면 중간 LEARN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력
# First Name : 정재현
# Last Name : 사랑해
# Country : Canada
# Subject : 퀴즈 완료하였습니다
# 6. 5초 대기 후 Submit 버튼 클릭
# 7. 5초 대기 후 브라우저 종료
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

# url 접속
browser.get("https://www.w3schools.com/")

# LEARN HTML 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# HOW TO 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()

# Contact Form 메뉴 클릭
# 가장 좋은 방법 (텍스트 전체 일치 여부 비교)
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
#browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[contains(text(),"Contact")]').click() # 일부 텍스트 비교
#browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]').click()

# 5. 입력란에 아래 값 입력
first_name = "정재현"
last_name = "사랑해"
country = "Canada"
subject = "퀴즈 완료하였습니다"
browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()
# 5초 대기 후 브라우저 종료
time.sleep(5)
browser.quit()