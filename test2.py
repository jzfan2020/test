#test for saving with json format
from bs4 import BeautifulSoup as bs
import requests as ss

url ='https://www.mobile01.com/topicdetail.php?f=455&t=6053710'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
res = ss.get(url, headers=headers)
soup = bs(res.text, 'html.parser')
output = []
obj={}
#印出po文日期
post_date = soup.select('li[class="l-toolBar__item"] span[class="o-fNotes o-fSubMini"]')[0].text
obj['post_date'] = post_date
#找出最後一頁:
page = soup.select('li[class="l-pagination__page"] a')
for j in range(len(page)):
    latest_page_num = max(page[j]['data-page'])
latest_page_num = int(latest_page_num)
#用剛剛抓出來得到的最終頁數指定新的url以爬下每一頁的評論內容
page_list = range(1, latest_page_num+1)
main = soup.select('div[itemprop="articleBody"]')[0].text.strip()

for k in page_list:
    url1 = url + '&p=%s'  %k
    print(url1)
    res1 = ss.get(url=url1, headers=headers)
    soup1 = bs(res1.text, 'html.parser')

    comments = soup1.select('div[class="u-gapBottom--max c-articleLimit"]')
    main += ';'

    for i in range(len(comments)):
        # print('---------comment{}---------'.format(i))
        # print(comments[i].text.strip())
        # main += '\n'
        # main += '-----------------------------------------'
        # main += '\n'
        # main += ';'
        main += comments[i].text.strip()
        main += ';'
        # main += '\n'
    obj['content'] = main


print(obj)
