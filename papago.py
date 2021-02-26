from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url) # get() 함수는 입력한 url 주소로 접속하는 함수이다.

time.sleep(3)
driver.close()