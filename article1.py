import requests
from bs4 import BeautifulSoup

news_url = 'https://search.hankyung.com/apps.frm/search.news?query=코로나'
raw = requests.get(news_url)

soup = BeautifulSoup(raw.text, 'html.parser')

box = soup.find('ul', {'class' : 'article'})
all_title = box.find_all('em', {'class' : 'tit'})

for title in all_title:
    t = title.text
    print(t.strip())