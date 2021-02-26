import requests
from bs4 import BeautifulSoup

lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

soup = BeautifulSoup(raw.text, 'html.parser') #html 코드로 해석하여 읽어라

box = soup.find('div', {'class' : 'nums'})
numbers = box.find_all('span')
print(numbers)

print("<최근 로또 당첨 번호>")
for i in numbers:
    print(i.text)

#print(box)
#print(soup)
#print(raw.text)
#print(raw)