#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_proxy_sites():
    proxysites = [

        {
            # 'url': 'http://ent.kuaidaili.com/api/getproxy/?orderid=938176699822329&num=1000&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=1&an_ha=1&format=json&sep=1',
            # 'url': 'http://dec.ip3366.net/api/?key=20171206101137832&getnum=1000&formats=2&proxytype=1',
            # back api
            'url': 'http://dev.25-88.cn/api/?key=20171206101137832&getnum=1000&formats=2&proxytype=1',
            'range': [],
            'pattern': '(?P<ip>(?:\d{1,3}\.){1,3}\d{1,3}):(?P<port>\d{1,5})'
        }
    ]
    # proxysites.extend(get_proxy_sites2())
    return proxysites


def get_proxy_sites2():
    import requests
    from bs4 import BeautifulSoup as BS
    from .config import HEADER
    sites = []

    url = 'http://blog.kuaidaili.com/'
    pattern = '(?P<ip>(?:\d{1,3}\.){1,3}\d{1,3}):(?P<port>\d{1,4})'
    r = requests.get(url, headers=HEADER)
    if r.ok:
        soup = BS(r.content, 'lxml')
        for s in soup.find_all('article')[:2]:
            sites.append({
                'url': s.find('a')['href'],
                'range': [],
                'pattern': pattern
            })
    return sites
