import csv

f = open('./covid19_articles.csv', 'r')

# CSV 파일의 모든 데이터를 변수 'rdr'에 저장
rdr = csv.reader(f)

# 'rdr'의 첫 번째는 건너뜀
next(rdr)

# 'rdr'에 저장된 데이터를 행별로 출력

for row in rdr:
    if '[속보]' in row[2]:
        print(row[2])

f.close()