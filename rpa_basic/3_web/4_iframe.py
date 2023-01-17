import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element(By.XPATH,'//*[@id="html"]') # 성공

elem.click()

browser.switch_to.default_content() # 상위로 빠져 나옴

elem = browser.find_element(By.XPATH, '//*[@id="html"]') # 실패

time.sleep(5) # 5초 대기

browser.quit()