# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 16:12
# @Author  : YuDong.Pang
import jieba
from data.mysql_jgh import *
from clean.inspect_company import *
from gensim_tfidf.test_tfidf import get_data
from collections import Counter


def stripword(seg):
    # 打开写入关键词的文件
    wordlist = []
    # 获取停用词表
    stop = open('key_word.txt', 'r+', encoding='utf-8')
    stopword = stop.read().split("\n")

    # 遍历分词表
    for key, flag in seg:
        # print(key,flag)
        # 去除人名
        if flag in ['nt', 'n']:
            # if flag in ['nt', 'nz', 'n','nt','vn','b','m','d','n','j','l','a','v','zg']:
            # 去除停用词，去除单字，去除重复词
            if not (key.strip() in stopword) and (len(key.strip()) > 1) and not (key.strip() in wordlist):
                wordlist.append(key)

    # 停用词去除END
    stop.close()
    print(wordlist)
    return wordlist


if __name__ == "__main__":
    count = 0
    for i in select_xfdata():
        company = clean_company_data(i[0])
        try:
            max_company = list(dict(Counter(company)).keys())[0]
        except:
            max_company = []
        if company:
            df = jieba.lcut(max_company)
            xsd, ds = get_data(df)
            if xsd[0] >= 0.8:
                count += 1
                print(max_company, xsd[0], ds[0])
            else:
                print(max_company)
    print(count)