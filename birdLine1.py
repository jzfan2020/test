import requests as ss
import json
from datetime import datetime
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# 取得 timestamp 給請求網址
ti = str(round(datetime.timestamp(datetime.today()) * 1000))
# print(ti)

# 設定頁數 換頁改這個就可以了 上限的話可能他網只會有 totalRows 設個判斷
page = 5

# 頁數部分是從開始給的 0 30 60 90 然後顯示個 大概!? 沒仔細算， url 裡面的 regionid 可以改變查詢區域 ，如果要代入篩選，可能要篩選後看看網址怎麼改，不過我們動的主要是 firstRow 這個參數  timestamp 是我們跟他請求 json 檔案需要提供的參數，從上面即時產生

url = 'https://sale.591.com.tw/home/search/list?type=2&shType=list&regionid=3&firstRow=' + str(
    (page - 1) * 30) + '&totalRows=42011&timestamp=' + ti

# 測試後只要 UserAgent 跟 X-CSRF-TOKEN 就可以過， 注意一下 X-CSRF 這有可能每天會改不確定 如果不能跑就檢查看看
headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
                'X-CSRF-TOKEN': 'LIaXM79BVNyMkK5sL0Sz8GTkpGPZCIP6hzFdGSPR'}

# cookie 可能會每天改也要檢查 整個直接複製就好
cookietmp = 'T591_TOKEN=1fc1afa6b61b808bb001a243d00d5e4b; tw591__privacy_agree=0; _ga=GA1.3.3888068.1581486339; __auc=d362b98817037ee74a89c8757cb; _ga=GA1.4.3888068.1581486339; _fbp=fb.2.1582342057546.216997220; _fbc=fb.2.1582342418975.IwAR3PIGNQ7b-sfEecvUpvet-gS3II8ox9kTn_bpLa9vIN1k3XSNhAZ9o_sKQ; is_new_index=1; is_new_index_redirect=1; webp=1; PHPSESSID=01fd1e87f03442acc2607db6e6856681; is_new_sale=1; new_rent_list_kind_test=1; user_index_role=2; urlJumpIp=3; urlJumpIpByTxt=%E6%96%B0%E5%8C%97%E5%B8%82; index_keyword_search_analysis=%7B%22role%22%3A%222%22%2C%22type%22%3A2%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; last_search_type=2; __utmc=82835026; __utmz=82835026.1583120508.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ba_cid=a%3A5%3A%7Bs%3A6%3A%22ba_cid%22%3Bs%3A32%3A%228a7241279ab7806970092658dd998bab%22%3Bs%3A7%3A%22page_ex%22%3Bs%3A48%3A%22https%3A%2F%2Frent.591.com.tw%2Frent-detail-8780430.html%22%3Bs%3A4%3A%22page%22%3Bs%3A92%3A%22https%3A%2F%2Fhelp.591.com.tw%2Fcontent%2F76%2F186%2Ftw%2F%25E9%259A%25B1%25E7%25A7%2581%25E6%25AC%258A%25E8%2581%25B2%25E6%2598%258E.html%22%3Bs%3A7%3A%22time_ex%22%3Bi%3A1583032261%3Bs%3A4%3A%22time%22%3Bi%3A1583126655%3B%7D; __utma=82835026.3888068.1581486339.1583120508.1583126656.2; new_housing_details=eyJpdiI6IkFTQ09GTVVRZ2M5SmFleFZqOEtUU3c9PSIsInZhbHVlIjoiREVCXC9HYjgwK3ZqTVZPcFpHbmlwM3c9PSIsIm1hYyI6IjlkZTYzMTgyOTdlNTA0NjM0NTFlYjdjZmU3NzE5ZDgzNTRmNDJlNzU0ZDVkNTJkNDE3ODJkZDczYTdkNDEwNTgifQ%3D%3D; 727bb8f81be702d344e84fb1bb764f6e=1; _gid=GA1.3.1090199590.1583250187; _gid=GA1.4.1090199590.1583250187; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7184757%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A6938881%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A6914834%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A7199739%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A6813319%3B%7D%7D; pt_s_28697119=vt=1583288797614&cad=; market_session=eyJpdiI6IlJqNmxNcmFCTFwvZnBSMENhcjUrVlJnPT0iLCJ2YWx1ZSI6InVoeEh1UXQ4NWNSNFpwZVp0Y2tseXBDU0hVbFFjXC9kWUhlalBRNUZDRDNpdzloeXFFVjhYU2FJbWVVK2RYZUxXIiwibWFjIjoiNDc0NmY4ODc5ZDgxZTBhNTlkY2NhMTNhMmRlYWMzMzVhMTQyMzg1MjQxOWYzNzNiNzgzNGRjYWIxMjExYWVkNSJ9; _gat_UA-97423186-1=1; pt_28697119=uid=jDawqXOd2O4ZrH4qQOwNuw&nid=0&vid=rXKkHdFQ37QYuYHqcrM/Qg&vn=30&pvn=1&sact=1583289850175&to_flag=0&pl=Odw8Cf6mt/Ccvwecoi8jKA*pt*1583289848219; _gat=1; d4acb7e09420bac327c314a2f788e718=1; _dc_gtm_UA-97423186-1=1; XSRF-TOKEN=eyJpdiI6IjloMlg4akU5eWIxdk1xOFNLS1RDZWc9PSIsInZhbHVlIjoiaGoyVVUybDZYWWQ3YkZJN2txb1VmMXZZcGdHMDR4YmdUeld2eklhcGVDekxnTjF4QndhcGpuSnEwckxnOTl4TTFodTE1UlFBVVVLTmhyMkFsdk1Zcmc9PSIsIm1hYyI6IjgxYmJjODc0ZTNiMTc3MGUzMGQ1MzY1YzNjNzBiNjZmM2I3ODAwNTYyNzQ2ZjFiZDBkNjYxMTIxODI5MmY3MDQifQ%3D%3D; 591_new_session=eyJpdiI6Im5PZEpvU3hoTVdvNE5ua3dyeEQ1bGc9PSIsInZhbHVlIjoiandBczBQXC9RSGtUbU9URlVHaFNCMWVBK0Jiem02VjBqNEM5bjNMM2locXBkWXg4R0xVcjgzMFBNMnY2eTcxTFl3NHlFXC8yT2piU2FVaklKdlpXRGQ1Zz09IiwibWFjIjoiYWU2YTI3NGQxMjU4ZDIxZmUxOTI2MzFlODMwNWJjMzViMmEwMDRmNWY2NzllZTg3MjQxNWEwMWFhNjllM2JhZiJ9'

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
for i in range(32):
    if "is_newhouse" in data[i].keys():
        pass

    else:
        sec = data[i]
        id = str(sec['houseid'])
        url_obj = 'https://sale.591.com.tw/home/house/detail/2/' + id +'.html'
        basic = {'名稱': sec['title'], '總坪數(含公設)': sec['area'],
                   '主建坪': sec['mainarea'],
                   '房間樓層/總樓層': sec['floor'], '格局': sec['room'],
                   '類型': sec['shape_name'],
                   '行政區': sec['section_name'],
                   '地址': sec['address'], '屋齡': sec['houseage'],
                   '總價': sec['price'], '每坪單價': sec['unitprice'], 'Tag': sec['tag'], '房仲網址': url_obj}

        res_obj = ss.get(url=url_obj, headers=headers)
        soup_obj = bs(res_obj.text, 'html.parser')
        a = soup_obj.select('div[class="detail-house-key"]')
        b = soup_obj.select('div[class="detail-house-value"]')

        output = []
        for ii in range(len(a)) :


            Obj = {}
            for j in range(len(b)):
                if ii == j:
                    for jj in range(1,len(a)):
                        # print(a[ii].text)
                        # print(b[j].text)
                        Obj[a[ii].text] = b[j].text
                else:
                    pass

            # 網頁內的

            # Obj[]


            output.append(Obj)


        print(output)

# 抓出每個物件的 houseid 然後串接進網址，這邊把抓到的第一個排除掉，因為他是推廣的新建案資料並非中古屋 可以把[]拿掉看 要注意就是 新建案網頁格式跟中古屋不太一樣
for j in sh:
    print(j)

    url = 'https://sale.591.com.tw/home/house/detail/2/' + hid + '.html'
    print(url)
    res_object = requests.get(url, headers = headers)
    soup = BeautifulSoup(res_object.text, 'html.parser')
print(data)