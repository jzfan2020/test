from bs4 import BeautifulSoup as bs
import requests as ss

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
url = 'https://sale.591.com.tw/home/house/detail/2/7397988.html'
res = ss.get(url, headers=headers)
soup = bs(res.text, 'html.parser')
# print(soup)
title = soup.select('div[class="detail-title-left"] h1')[0].text.strip()
print(title)
current_price = soup.select('span[class="info-price-num"]')[0].text.strip()

single_price = soup.select('div[class="info-price-per"]')[0].text
# print(single_price.split(':')[0].split(':'))
basic = soup.select('div[class="info-floor-key"]')
basic_k = soup.select('div[class="info-floor-value"]')
floor = soup.select('span[class="info-addr-key"]')
floor_v = soup.select('span[class="info-addr-value"]')
detail = soup.select('div[class="detail-house-key"]')
detail_v = soup.select('div[class="detail-house-value"]')
life = soup.select('div[class="detail-house-name"]')
life_v = soup.select('div [class="detail-house-life"]')
# print(life)

output=[]
oth ={}
def obd(x, y):
    for i in range(len(x)):
        obj = {}
        for j in range(len(y)):
            if i == j:
                obj[x[i].text] = y[j].text
                output.append(obj)
other1=""
if len(detail_v)-len(detail) != 0:
    other_v = detail_v[len(detail)::]

    for i in range(len(other_v)):
        other1 += other_v[i].text + " "

oth['物件'] = title
oth['售價'] = current_price
oth['單價']=single_price[3::]
output.append(oth)
a = obd(basic_k, basic)
a = obd(floor, floor_v)
a = obd(detail, detail_v)

life1 =""
det = {}
for i in range(len(life_v)):
    life1 += (life_v[i].text + ' ')

for i in range(len(life)):
    if life[i].text == '生活機能':
        det[life[i].text] = life1
    if life[i].text == '附近交通':
        det[life[i].text] = other1


output.append(det)
print(output)
