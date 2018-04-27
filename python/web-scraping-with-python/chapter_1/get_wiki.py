#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages = set()


def get_links(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bs = BeautifulSoup(html)
    try:
        print(bs.h1.get_text())
        print(bs.find(id = "mw-content-text").findAll("p")[0])
        print(bs.find(id = "ca-edit").find("span").find("a").attrs['href'])
    except AttributeError: \
            print("页面缺少一些属性!不过不用担心!")
    for link in bs.findAll("a", href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print("----------------\n" + newPage)
                pages.add(newPage)
                get_links(newPage)

get_links("")
