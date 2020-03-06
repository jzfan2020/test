import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
import os
import random
import  time
path = r'./res_501_2hand'
if not os.path.exists(path):
    os.mkdir(path)
def obj_append(x, y):
    for j in range(len(x)):
        for k in range(len(y)):
            if j == k:
                obj[x[j].text] = y[k].text


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
# 取得 timestamp 給請求網址
ti = str(round(datetime.timestamp(datetime.today()) * 1000))
# print(ti)

# 設定頁數 換頁改這個就可以了 上限的話可能他網只會有 totalRows 設個判斷
page = 200

# 頁數部分是從開始給的 0 30 60 90 然後顯示個 大概!? 沒仔細算， url 裡面的 regionid 可以改變查詢區域 ，如果要代入篩選，可能要篩選後看看網址怎麼改，不過我們動的主要是 firstRow 這個參數  timestamp 是我們跟他請求 json 檔案需要提供的參數，從上面即時產生
for i in range(page):
    url = 'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=3&kind=9&firstRow=' + str((i) * 30) + '&totalRows=42011&timestamp=' + ti
    print('第{}頁'.format(i))
    output = []
    # 測試後只要 UserAgent 跟 X-CSRF-TOKEN 就可以過， 注意一下 X-CSRF 這有可能每天會改不確定 如果不能跑就檢查看看
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                'X-CSRF-TOKEN': 'JrIlLW3mEmYtAzZn29H0ST4ebmYLtQaGdlnFgNWq'}

    # cookie 可能會每天改也要檢查 整個直接複製就好
    cookietmp = 'is_new_index=1; is_new_index_redirect=1; T591_TOKEN=pjhtlsfkuvdldscpnd1b7oj5m0; _ga=GA1.3.944247625.1582985233; tw591__privacy_agree=0; _ga=GA1.4.944247625.1582985233; _fbp=fb.2.1582985248542.304671003; urlJumpIp=3; urlJumpIpByTxt=%E6%96%B0%E5%8C%97%E5%B8%82; user_index_role=2; last_search_type=2; new_housing_details=eyJpdiI6ImMwYktvYUpaa1dmdU83THN1cXJ5NWc9PSIsInZhbHVlIjoiN2VMQW1saHprSGtTblVnOHlna0ZhQT09IiwibWFjIjoiYzAxYzAwNzUzZjgzZjgzNDYxNGMxOTAxZDcyMWRjNmNmOTZlZDYzNzQ1NjQ4MzM2ZTQ4ZGRlNzhkYTI1YWI1MyJ9; webp=1; PHPSESSID=co4tnr5ugsump427p1r7cmum43; _gid=GA1.3.1030144375.1583422617; index_keyword_search_analysis=%7B%22role%22%3A%222%22%2C%22type%22%3A2%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; user_sessionid=co4tnr5ugsump427p1r7cmum43; is_new_sale=1; f9988a6b68615a6bced5d2da8c426769=1; _gid=GA1.4.1030144375.1583422617; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A6854337%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7184757%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7198734%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7368962%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A6938881%3B%7D%7D; pt_s_28697119=vt=1583427603238&cad=; pt_28697119=uid=dWEnE6U3hCCfgFFuWNGwkQ&nid=0&vid=ZYMgG7m09KTWr74QD2aLtg&vn=9&pvn=1&sact=1583463089564&to_flag=0&pl=Odw8Cf6mt/Ccvwecoi8jKA*pt*1583463089526; 0ac3129b6eda41fcddbd94eda67471b5=1; _gat=1; _dc_gtm_UA-97423186-1=1; _gat_UA-97423186-1=1; 591_new_session=eyJpdiI6IkJkeXdhUEhuMmtZWDhGNW5HVk5qWlE9PSIsInZhbHVlIjoiblllN2NJRFRGVUdpaHp6QW9GenhTcWdFcWl0SDA3NVNmd1lLaHNCUkVOR0h2MTlJV21wdVArYW9idWF5bWZHczhnTzRra0hjbHRpdjV4Y0pjeHZkd0E9PSIsIm1hYyI6Ijg5N2E5ODJkYjc4YzYyZmUyYTNlODEyMjlhZWVlZThhNjY1YzZkMzdlNDkxNjk3NWVjYWUzMWMyMjRjY2I3OTkifQ%3D%3D'

    # 將cookies 轉成字典形式
    cookies = {}
    for u in cookietmp.split(';'):
        cookies[u.split('=')[0]] = u.split('=')[1]

    # 請求網址 並用 json解析
    res = requests.get(url, headers=headers1, cookies=cookies)
    data = json.loads(res.text)['data']['house_list']
    # print(data)
    # print(json.dumps(data[0], ensure_ascii=False), '\n')
    # print(json.dumps(data[1], ensure_ascii=False), '\n')
    # print(json.dumps(data[2], ensure_ascii=False), '\n')

    # 抓出每個物件的 houseid 然後串接進網址，這邊把抓到的第一個排除掉，因為他是推廣的新建案資料並非中古屋 可以把[]拿掉看 要注意就是 新建案網頁格式跟中古屋不太一樣

    for j in range(len(data)):
        obj = {}
        if "is_newhouse" in data[j].keys():
            pass
        else:
            hand2 = data[j]
            id = str(hand2['houseid'])
            url_obj = 'https://sale.591.com.tw/home/house/detail/2/' + id + '.html'
            print(url_obj)
            res_object = requests.get(url=url_obj, headers = headers)
            soup = BeautifulSoup(res_object.text, 'html.parser')
            #開始嘗試取各物件的資料





            title = soup.select('h1[class="detail-title-content"]')[0].text.strip()

            price = soup.select('span[class="info-price-num"]')[0].text

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
            trans = soup.select('div[class="detail-house-value"]')

            obj['物件'] = title
            obj['售價'] = price
            obj['單價'] = single_price
            a = obj_append(basic_k, basic)
            b = obj_append(floor, floor_v)
            c = obj_append(detail, detail_v)

            life1 = ""
            for t in range(len(life_v)):
                life1 += (life_v[t].text + ' ')

            trans1 = ""

            for l in range(len(life)):
                if life[l].text == '生活機能':
                    obj[life[l].text] = life1
                elif life[l].text == '附近交通':
                    if len(detail_v) - len(detail) != 0:
                        for p in range(len(detail_v)):
                            if p >= len(detail):
                                trans1 += (detail_v[p].text + ' ')
                    obj[life[l].text] = trans1

            # print(obj)
            output.append(obj)
            time.sleep(random.uniform(0.5, 2.8))
    s = str(output)

    with open(path + '/' + 'No.{}'.format(i) + '.txt', 'w', encoding='utf-8') as f:
        f.write(s)

    print(output)


    # print(url_obj)





