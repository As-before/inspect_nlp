# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 14:27
# @Author  : YuDong.Pang
# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 17:59
# @Author  : YuDong.Pang
from gensim import corpora,similarities,models
import jieba.posseg as psg
import jieba


def chinese_word_psg_cut(mytext):
    '''
    使用jieba分词并去除停用词
    :param mytext: 文本
    :return:
    '''
    # 生成去停用词列表
    stopwords = [line.strip() for line in open('../config/key_word.txt', 'r', encoding='utf-8').readlines()]
    seg_list = []
    seg_text = jieba.lcut(mytext)
    for word,flag in seg_text:
        if flag in ['ns']:
            continue
        if word not in stopwords:
            seg_list.append(word)
    return seg_list

def chinese_word_cut(mytext):
    '''
    使用jieba分词
    :param mytext: 文本
    :return:
    '''
    seg_text = jieba.lcut(mytext)
    return seg_text

def get_file(path = '../config/company.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
    return data

def run():
    train = []
    train_item_id = []
    for id,line in enumerate(get_file()):
        # 分词
        line = chinese_word_cut(line)
        train.append(line)
        train_item_id.append(id)
    dictionary = corpora.Dictionary(train)
    corpus = [dictionary.doc2bow(text) for text in train]
    # corpus是一个返回bow向量的迭代器。下面代码将完成对corpus中出现的每一个特征的IDF值的统计工作
    tfidf_model = models.TfidfModel(corpus, dictionary=dictionary)
    corpus_tfidf = tfidf_model[corpus]
    dictionary.save('../model/train_dictionary.dict')  # 保存生成的词典
    tfidf_model.save('../model/train_tfidf.model')
    corpora.MmCorpus.serialize('../model/train_corpuse.mm', corpus)
    featurenum = len(dictionary.token2id.keys())  # 通过token2id得到特征数
    # 稀疏矩阵相似度，从而建立索引,我们用待检索的文档向量初始化一个相似度计算的对象
    index = similarities.SparseMatrixSimilarity(corpus_tfidf, num_features=featurenum)
    index.save('../model/train_index.index')
    # pickle.dump(train_item_id,open('item_id1.pkl','wb'))

if __name__ == "__main__":
    run()