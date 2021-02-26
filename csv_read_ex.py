import csv

# 작성할 'example.csv' 파일을 생성하여 변수 'f'에 저장
f = open('./example.csv', 'r')

# CSV 파일의 모든 데이터를 변수 'rdr'에 저장
rdr = csv.reader(f)

# 'rdr'의 첫 번째는 건너뜀
next(rdr)

# 'rdr'에 저장된 데이터를 행별로 출력
for row in rdr:
    print(row)

f.close()