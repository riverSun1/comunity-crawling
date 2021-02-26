# 라이브러리 import
from selenium import webdriver
import time

# 검색 키워드 입력
keyword = input('뉴스 검색 키워드 : ')

# 뉴스 기사 게시판 접속
driver = webdriver.Chrome('./chromedriver')
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)

# 단순히 뉴스마다 번호를 붙여주기 위한 변수
count = 0
#//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[1]
# //*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[1]
for i in range(1, 4):
    driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/div/span/a[' + str(i) + ']').click()
    time.sleep(1)

    # 모든 <em.tit> 태그를 'ten_articles' 변수에 저장
    ten_articles = driver.find_elements_by_css_selector('em.tit')

    # 10개 뉴스 기사를 대상으로 반복문 실행
    for article in ten_articles:
	    # 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, text는 제목을 나타냄
        title = article.text

        # 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, 클릭하면 뉴스 기사 본문을 확인할 수 있음
        article.click()
	    # 시간적 여유 원하는 만큼
        time.sleep(1)

	    # 'driver'를 새로운 탭 (뉴스 기사 본문)으로 전환
        driver.switch_to.window(driver.window_handles[-1])

    	# 기사 본문을 'content' 변수에 저장
        content = driver.find_element_by_id('articletxt').text

        # 'content'를 '\n' 단위로 나누어 'seperate' 변수에 저장
        seperate = content.split('\n')

    	# 기사 본문 출력
        count += 1
        print(f'< {count}번 뉴스 - {title} >')

        for sep in seperate:
            # 아무 것도 없는 공백 ('')이 포함되어 있기 때문에, 이런 공백은 출력하지 않음
            if sep != '':
                # print(값, end = ??)를 활용하여 모든 sep 사이에 공백 한 칸 (' ')을 삽입하여 출력
                print(sep, end=' ')
        # 하나의 본문 내용을 출력하고 나면 줄 간격을 한 줄 넣어줌
        print('\n')

    	# 새로운 탭 (뉴스 기사 본문)에서 작업을 다 했으므로, 새로운 탭은 닫아줌
        driver.close()

	    # 다시 'driver'를 맨 처음 탭으로 전환
        driver.switch_to.window(driver.window_handles[0])

	    # 시간적 여유 원하는 만큼
        time.sleep(1)

# 크롬 창 닫기
driver.close()