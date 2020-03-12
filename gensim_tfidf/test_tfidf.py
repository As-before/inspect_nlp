# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 15:21
# @Author  : YuDong.Pang
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, similarities, models

def get_data(test):
    '''
    返回识别的文本
    :param test: 要识别的文本
    :return: xsdList 可信度
    :return: datas 识别文本
    '''
    dictionary = corpora.Dictionary.load("../model/train_dictionary.dict")
    tfidf = models.TfidfModel.load("../model/train_tfidf.model")
    index = similarities.SparseMatrixSimilarity.load('../model/train_index.index')
    # 产生BOW向量
    vec = dictionary.doc2bow(test)
    # 生成tfidf向量
    test_vec = tfidf[vec]
    # 计算相似度
    sim = index.get_similarities(test_vec)
    result_list = sorted(enumerate(sim), key=lambda student : student[1],reverse=True)[0:5]
    xsdlist = []
    with open('../config/company.txt','r',encoding='utf-8') as f:
        datass = f.read().split('\n')
    datas = []
    for k,y in result_list:
        datas.append(datass[k])
        xsdlist.append(y)
    return xsdlist,datas