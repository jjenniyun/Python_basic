import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element(By.XPATH,'//*[@id="html"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않다면
    print("선택이 안됨")
    elem.click()
else: # 라디오 버튼 선택되어 있다면
    print("선택됨")
    
time.sleep(5) # 5초 대기

if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않다면
    print("선택이 안됨")
    elem.click()
else: # 라디오 버튼 선택되어 있다면
    print("선택됨")
    
browser.quit()