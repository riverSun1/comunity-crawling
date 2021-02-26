# my_papago.csv 에 저장된 번역 결과 (한국어)를 파파고에 입력해서 번역 결과 (영어)를 출력하기﻿
# student apple computer programming doll breakfast lunch dinner

from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver')
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)

# 읽어올 'my_papago.csv' 파일을 변수 'f'에 저장
f = open('./my_papago.csv', 'r')

# CSV 파일의 모든 데이터를 변수 'rdr'에 저장
rdr = csv.reader(f)

# 'rdr'의 첫 번째 (열 제목)는 건너뜀
next(rdr)

# 딕셔너리 생성
my_dict = []

# 딕셔너리에 한글 번역 결과만 저장
for row in rdr:
    my_dict.append(row[1])
f.close()

# 번역 언어 전환버튼 클릭
driver.find_element_by_css_selector('button.btn_switch___x4Tcl')

# 번역 결과 출력
for keyword in my_dict:
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(keyword)
    # 번역 버튼 클릭
    driver.find_element_by_css_selector('button#btnTranslate').click()
    time.sleep(1)
    # 번역 결과 저장, 출력
    output = driver.find_element_by_css_selector('div#txtTarget').text
    print(keyword, ':', output)
    # 입력 칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()

# 파일 닫기
driver.close()