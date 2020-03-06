import requests as ss
import json
from datetime import datetime
from bs4 import BeautifulSoup as bs
import time
import random
import os

def obd(x, y):
    for i in range(len(x)):
        obj = {}
        for j in range(len(y)):
            if i == j:
                obj[x[i].text] = y[j].text
                output.append(obj)

path = r'./current_res_591'
if not os.path.exists(path):
    os.mkdir(path)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# 取得 timestamp 給請求網址

# print(ti)

# 設定頁數 換頁改這個就可以了 上限的話可能他網只會有 totalRows 設個判斷
page = 100

# 頁數部分是從開始給的 0 30 60 90 然後顯示個 大概!? 沒仔細算， url 裡面的 regionid 可以改變查詢區域 ，如果要代入篩選，可能要篩選後看看網址怎麼改，不過我們動的主要是 firstRow 這個參數  timestamp 是我們跟他請求 json 檔案需要提供的參數，從上面即時產生
for i in range(page):
    print('第{}頁'.format(i+1))

    ti = str(round(datetime.timestamp(datetime.today()) * 1000))
    url = 'https://sale.591.com.tw/home/search/list?type=2&shType=list&kind=9&regionid=3&firstRow=' + str(i * 30) + '&totalRows=40799&timestamp=' + ti
    # print(url)

    # 測試後只要 UserAgent 跟 X-CSRF-TOKEN 就可以過， 注意一下 X-CSRF 這有可能每天會改不確定 如果不能跑就檢查看看
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'X-CSRF-TOKEN': 'JslWbWEpLIJKO4tlpkOoCfhsgavYF4kESBa30TOs'}
    #
    # cookie 可能會每天改也要檢查 整個直接複製就好
    cookietmp = 'T591_TOKEN=1fc1afa6b61b808bb001a243d00d5e4b; tw591__privacy_agree=0; _ga=GA1.3.3888068.1581486339; __auc=d362b98817037ee74a89c8757cb; _ga=GA1.4.3888068.1581486339; _fbp=fb.2.1582342057546.216997220; _fbc=fb.2.1582342418975.IwAR3PIGNQ7b-sfEecvUpvet-gS3II8ox9kTn_bpLa9vIN1k3XSNhAZ9o_sKQ; is_new_index=1; is_new_index_redirect=1; webp=1; PHPSESSID=01fd1e87f03442acc2607db6e6856681; is_new_sale=1; new_rent_list_kind_test=1; user_index_role=2; urlJumpIp=3; urlJumpIpByTxt=%E6%96%B0%E5%8C%97%E5%B8%82; index_keyword_search_analysis=%7B%22role%22%3A%222%22%2C%22type%22%3A2%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; last_search_type=2; __utmc=82835026; __utmz=82835026.1583120508.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ba_cid=a%3A5%3A%7Bs%3A6%3A%22ba_cid%22%3Bs%3A32%3A%228a7241279ab7806970092658dd998bab%22%3Bs%3A7%3A%22page_ex%22%3Bs%3A48%3A%22https%3A%2F%2Frent.591.com.tw%2Frent-detail-8780430.html%22%3Bs%3A4%3A%22page%22%3Bs%3A92%3A%22https%3A%2F%2Fhelp.591.com.tw%2Fcontent%2F76%2F186%2Ftw%2F%25E9%259A%25B1%25E7%25A7%2581%25E6%25AC%258A%25E8%2581%25B2%25E6%2598%258E.html%22%3Bs%3A7%3A%22time_ex%22%3Bi%3A1583032261%3Bs%3A4%3A%22time%22%3Bi%3A1583126655%3B%7D; __utma=82835026.3888068.1581486339.1583120508.1583126656.2; new_housing_details=eyJpdiI6IkFTQ09GTVVRZ2M5SmFleFZqOEtUU3c9PSIsInZhbHVlIjoiREVCXC9HYjgwK3ZqTVZPcFpHbmlwM3c9PSIsIm1hYyI6IjlkZTYzMTgyOTdlNTA0NjM0NTFlYjdjZmU3NzE5ZDgzNTRmNDJlNzU0ZDVkNTJkNDE3ODJkZDczYTdkNDEwNTgifQ%3D%3D; 727bb8f81be702d344e84fb1bb764f6e=1; _gid=GA1.3.1090199590.1583250187; _gid=GA1.4.1090199590.1583250187; d4acb7e09420bac327c314a2f788e718=1; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7155527%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7370312%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A6938881%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7276837%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7184757%3B%7D%7D; pt_s_28697119=vt=1583293181743&cad=; pt_28697119=uid=jDawqXOd2O4ZrH4qQOwNuw&nid=0&vid=CTON-bxGZL7Z8W4xnd3PCA&vn=33&pvn=2&sact=1583293181743&to_flag=1&pl=9k-MixeDsRrGVGFKHu4veg*pt*1583293181743; _gat_UA-97423186-1=1; _gat=1; _dc_gtm_UA-97423186-1=1; XSRF-TOKEN=eyJpdiI6IlFWMlJpblMxU2JiMnVSRTV4NlVlV3c9PSIsInZhbHVlIjoieG5UMEhkbndXZE9TSktGRXF2TGNXUmp6MUZUVDdwQUZ6eWs0UVNJT1V6VnU4dURjMVwvQnV2WG5TTUwwMjFCN0VWbzFsM2JIcncwZHVjWnhpS0VzODBBPT0iLCJtYWMiOiJjZTY1OTQ3ZGMwNGFkZmRhMGFmZmE0ZmVkODUzMjU1NTRhZWZjZjQwMmQzOTVjY2E5MTdjMzc0YmJhOWVmNTcyIn0%3D; 591_new_session=eyJpdiI6IkJORUFyUEpVNTFZTVM2R29EaUs0NEE9PSIsInZhbHVlIjoiWERWM2RDREl6cmNcLzRqYXVpY05qVE5qanJURFQ1cm9LVzdcL2R0R3J6N1RYa1J0dFRiSkNCY2cyVVY2ZnFNQVk3M3IrN05QUThSZWJobWR6SE1JXC82ZWc9PSIsIm1hYyI6IjdkMTdhMDM4NDMwZWNmZDUzYTM4YzNkMjk4Y2FiZjJiMWY4MGFlOGQ2YTJiNGY0ZTFhMzI5MGIyNWI3OTc0NGYifQ%3D%3D'

    # 將cookies 轉成字典形式
    cookies = {}
    for i in cookietmp.split(';'):
        cookies[i.split('=')[0]] = i.split('=')[1]

    # 請求網址 並用 json解析
    res = ss.get(url, headers=headers1, cookies=cookies)
    data = json.loads(res.text)['data']['house_list']

    # print(json.dumps(data[1], ensure_ascii = False))
    # print(json.dumps(data[2], ensure_ascii = False))
    #
    Obj = {}

    j = 0
    while True:
        try:
            if data[j]:
                pass
        except:
            break

        if "is_newhouse"  in data[j].keys():
            pass
        else:
            sec = data[j]
            id = str(sec['houseid'])

            url_obj = 'https://sale.591.com.tw/home/house/detail/2/' + id + '.html'

            res_obj = ss.get(url=url_obj, headers=headers)
            soup = bs(res_obj.text, 'html.parser')
            print(url_obj)

            title = soup.select('div[class="detail-title-left"] h1')[0].text.strip()

            current_price = soup.select('span[class="info-price-num"]')[0].text

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

            output = []
            oth = {}

            other1 = ""
            if len(detail_v) - len(detail) != 0:
                other_v = detail_v[len(detail)::]

                for k in range(len(other_v)):
                    other1 += other_v[k].text + " "

            oth['物件'] = title
            oth['售價'] = current_price
            oth['單價'] = single_price[3::]
            output.append(oth)
            a = obd(basic_k, basic)
            a = obd(floor, floor_v)
            a = obd(detail, detail_v)

            life1 = ""
            det = {}
            for k in range(len(life_v)):
                life1 += (life_v[k].text + ' ')

            for k in range(len(life)):
                if life[k].text == '生活機能':
                    det[life[k].text] = life1
                if life[k].text == '附近交通':
                    det[life[k].text] = other1

            output.append(det)
            s = str(output)
            # print(type(a))

            with open(path + '/' + id + '.txt', 'w', encoding='utf-8') as f:
                f.write(s)

            time.sleep(random.uniform(0.5, 2.8))

            j += 1
            print('complete')




    # print(url_obj)
