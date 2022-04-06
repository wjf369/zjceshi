# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import os


def getHTMLText(url):
    try:
        req = requests.get(url, timeout=30)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        return req.text
    except:
        return"有异常"
    finally:
        print(req.encoding)
        print(req.raise_for_status())


if __name__ == "__main__":
    url = "https://www.jianshu.com/p/2f190ab5a869"
    print(getHTMLText(url))

    # https: // www.jianshu.com /