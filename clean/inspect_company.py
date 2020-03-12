# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 14:25
# @Author  : YuDong.Pang
import re
from bs4 import BeautifulSoup
import html


def clean_company_html(text):
    '''
    获取网页中的公司名称
    :param text: 接受一个网页文本格式
    :return: 识别到的所有公司名称
    '''
    soup = BeautifulSoup(html.unescape(text), 'lxml')
    # 去除属性ul
    [s.extract() for s in soup("style")]
    # 去除属性svg
    [s.extract() for s in soup("svg")]
    # 去除属性script
    [s.extract() for s in soup("script")]
    # 获取城市列表
    with open('config/city.txt', 'r', encoding='utf-8') as f:
        city = f.read().replace('： ', ' ').replace('\n', '').replace(' ', ',')
    data = soup.text.replace('\n', '').replace(' ', '').replace(',', '').replace('：', '')
    data = re.sub("[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]", '', data)
    company = []
    for i in (re.finditer('公司', data)):
        start = i.start()
        end = i.end()
        ns = data[start - 15:end]
        for ci in city.split(','):
            for cic in re.finditer(ci, ns):
                company.append(ns[cic.start():])
    for i in (re.finditer('集团', data)):
        start = i.start()
        end = i.end()
        ns = data[start - 8:end]
        for ci in city.split(','):
            for cic in re.finditer(ci, ns):
                company.append(ns[cic.start():])
    return company


def clean_company_data(text):
    '''
    获取文本中所有的公司名称
    :param text: 文本
    :return: 识别到的所有公司名称
    '''
    with open('config/city.txt', 'r', encoding='utf-8') as f:
        city = f.read().replace('： ', ' ').replace('\n', '').replace(' ', ',')
    data = text.replace('\n', '').replace(' ', '').replace(',', '').replace('：', '')
    data = re.sub("[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]", '', data)
    company = []
    for i in (re.finditer('公司', data)):
        start = i.start()
        end = i.end()
        ns = data[start - 15:end]
        for ci in city.split(','):
            for cic in re.finditer(ci, ns):
                company.append(ns[cic.start():])
    for i in (re.finditer('集团', data)):
        start = i.start()
        end = i.end()
        ns = data[start - 8:end]
        for ci in city.split(','):
            for cic in re.finditer(ci, ns):
                company.append(ns[cic.start():])
    return company
