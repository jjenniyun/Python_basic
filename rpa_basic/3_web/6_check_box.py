import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame('iframeResult')

#elem = browser.find_element(By.XPATH,'//*[@id="vehicle1"]')
elem = browser.find_element(By.ID,'vehicle1')

time.sleep(5)

if elem.is_selected == False:
    print("선택 안됨")
    elem.click()
else:
    print("선택됨")

browser.quit()
