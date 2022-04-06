# from urllib import request
# import requests
# from lxml import etree
# import re
# from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import os


if __name__ =="__main__":
    #需求：
    url='https://www.bqkan.com/70_70215/460328505.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
    }

    download_res = requests.get(url=url, headers=headers)
    ht = download_res.text
    soup_texts = BeautifulSoup(ht, 'html.parser')
    # print(soup_texts)
    texts = soup_texts.find_all(id='content', class_='showtxt')
    soup_text = BeautifulSoup(str(texts), 'lxml').div.text.replace('\xa0', '')
    print(soup_text)