from selenium import webdriver
import time

# 나만의 번역 사전 생성
my_dict = {}

# 자동화된 크롬 창 실행
driver = webdriver.Chrome('./chromedriver')

papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

def get_papago_result():
    question = input('번역할 영단어 입력 : ')
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text

    # 번역 사전에 저장 및 출력
    my_dict[question] = output
    driver.find_element_by_css_selector('textarea#txtSource').clear()

for i in range(5):
    get_papago_result()

print(my_dict)
# print('번역 결과 :', output)

driver.close()