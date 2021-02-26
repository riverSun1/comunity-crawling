# 라이브러리 import
from selenium import webdriver
import time

# 자동화된 크롬 창 실행
driver = webdriver.Chrome('./chromedriver')

# 네이버 로그인 페이지 접속
login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)

# 시간적 여유 원하는 만큼
time.sleep(2)

# 본인의 아이디, 비밀번호를 각각 변수에 저장
# ex) 아이디 : comu, 비밀번호 : 12345
my_id = 'comu'
my_pw = '12345'

# 아이디와 비밀번호 입력
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + my_pw + "\'")
time.sleep(1)

# '로그인' 버튼 클릭
driver.find_element_by_id('log.login').click()

# 시간적 여유 원하는 만큼
time.sleep(1)

# 코뮤니티 접속
comu_url = 'https://cafe.naver.com/codeuniv'
driver.get(comu_url)
time.sleep(1)

# '신규회원게시판' 클릭
driver.find_element_by_id('menuLink90').click()

# 시간적 여유 원하는 만큼
time.sleep(1)

# 프레임 전환
driver.switch_to.frame('cafe_main')

# 시간적 여유 원하는 만큼
time.sleep(1)

# 첫번째 글 클릭
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()

# 시간적 여유 원하는 만큼
time.sleep(1)

# 글 내용 출력
content = driver.find_element_by_css_selector('div.se-component-content').text
print('< ', '1', '번째 글 >')
print(content, '\n')

for i in range (2, 21):
    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(3)
    content = driver.find_element_by_css_selector('div.se-component-content').text
    print('< ', i,'번째 글 >')
    print(content, '\n')

# 크롬 창 닫기
driver.close()