import requests
from bs4 import BeautifulSoup

keyword = input("키워드를 입력해주세요 : ")
count = 0

for page in range(1,3):
  news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM​&page=' + str(page)
  raw = requests.get(news_url)

  soup = BeautifulSoup(raw.text, 'html.parser')

  box = soup.find('ul', {'class' : 'article'})
  all_title = box.find_all('em', {'class' : 'tit'})
  all_date = box.find_all('span', {'class' : 'date_time'})

  for i in range(10):
    count += 1
    print(count, '- [', all_date[i].text + ' ]', all_title[i].text.strip())