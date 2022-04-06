from urllib import request
import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
if __name__ =="__main__":
    #需求：爬取全国城市名
    url='https://www.bqkan.com/70_70215/460328505.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
    }

    download_req = request.Request(url=url, headers=headers)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk', 'ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    print(soup_texts)
    texts = soup_texts.find_all(id='content', class_='showtxt')
    soup_text = BeautifulSoup(str(texts), 'lxml').div.text.replace('\xa0', '')
    # print(soup_text)











    #
    # page_text = requests.get(url=url, headers=headers).text
    # bs = BeautifulSoup(page_text, 'html.parser')  # 初始化BeautifulSoup库,并设置解析器

    # for item in bs.find_all("a"):
    #     print(item.get_text())
    # bs.select('div[class="bottom"]')
    # print(bs.select('div[class="col-lg-9 col-md-8 col-sm-8 col-xs-12"]'))
    # print(bs.select('div[class="col-lg-9 col-md-8 col-sm-8 col-xs-12"]')[0].get_text())
    # for title in bs.select('ul[class="unstyled"]'):
    #
    #     print(title.get_text())



    # tree = etree.HTML(page_text)
    # li_list = tree.xpath('//div[class="bottom"]/ul/li/a | //div[class="bottom"]/ul/div[2]/li/a')
    # all_city_name = []
    # for a in li_list:
    #         city_name = a.xpath('./text()')[0]
    #         all_city_name.append(city_name)
    # print(all_city_name,len(all_city_name))
    # print("爬起成功") class="bottom"  class="col-lg-9 col-md-8 col-sm-8 col-xs-12"