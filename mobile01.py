import requests as ss
from bs4 import BeautifulSoup as bs
import time
import os
import random

path = r'./new_tpe_202004'
if not os.path.exists(path):
    os.mkdir(path)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
#進入討論區主頁面並設定欲爬取的頁面數量
for i in range(1, 472):
    output = []
    url = 'https://www.mobile01.com/topiclist.php?f=455&p=%s' %i
    # print(url)
    res = ss.get(url, headers=headers)
    soup = bs(res.text, 'html.parser')
    title = soup.select('div[class="c-listTableTd__title"] a')
#存取每個討論的文章title並進入其文章存取討論內容
    for each_title in title:
        obj = {}
        try:
            int(each_title.text)
        except ValueError as e:
            obj['title'] = each_title.text
            article_id = each_title['href'].split('t=')[1]
            obj['id'] = article_id
            each_url = 'https://www.mobile01.com/'+ (each_title['href'])
            obj['url'] = each_url
            res_each = ss.get(url=each_url, headers=headers)
            res_soup = bs(res_each.text, 'html.parser')

            # 印出po文日期
            post_date = res_soup.select('li[class="l-toolBar__item"] span[class="o-fNotes o-fSubMini"]')[0].text
            obj['post_date'] = post_date
            # 找出最後一頁:
            page = res_soup.select('li[class="l-pagination__page"] a')
            for j in range(len(page)):
                latest_page_num = max(page[j]['data-page'])
            latest_page_num = int(latest_page_num)

            # 用剛剛抓出來得到的最終頁數指定新的url以爬下每一頁的評論內容
            page_list = range(1, latest_page_num + 1)
            main = res_soup.select('div[itemprop="articleBody"]')[0].text.strip()

            for k in page_list:
                url1 = each_url + '&p=%s' % k
                # print(url1)
                res1 = ss.get(url=url1, headers=headers)
                soup1 = bs(res1.text, 'html.parser')

                comments = soup1.select('div[class="u-gapBottom--max c-articleLimit"]')
                main += ';'
                for l in range(len(comments)):
                    # print('---------comment{}---------'.format(l))
                    # print(comments[l].text.strip())
                    # main += '\n'
                    # main += '-----------------------------------------'
                    # main += '\n'
                    # main += ';'
                    main += comments[l].text.strip()
                    main += ';'
                    # main += '\n'
                obj['content'] = main
            output.append(obj)
            time.sleep(random.uniform(0.5, 1.1))

    s = str(output)

    with open(path + '/' + 'No_{}'.format(i) + '.txt', 'w', encoding='utf-8') as f:
        f.write(s)

    print(output)

