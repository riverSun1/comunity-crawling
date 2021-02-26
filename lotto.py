# requests 패키지 import
import requests
# bs4에 있는 BeautifulSoup import
from bs4 import BeautifulSoup
lotto_url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(lotto_url)

# 실제 html 코드로 해석하여 읽어라
soup = BeautifulSoup(raw.text, 'html.parser')

# 큰 틀 <div class = "nums"> 선택
box = soup.find('div', {'class' : 'nums'})
# 큰 틀안에 있는 <span>태그 모두 가져오기
numbers = box.find_all('span')

# 한줄씩 출력
print("<최근 로또 당첨 번호>")
for i in numbers:
    print(i.text)