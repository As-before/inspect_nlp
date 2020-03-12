# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 15:38
# @Author  : YuDong.Pang
from flask import Flask, render_template, Response
import numpy as np
from flask import request
from gensim_tfidf.test_tfidf import get_data
import jieba
import json

app = Flask(__name__)
app.debug = True

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

@app.route('/')
def index():
    return 'Hello world'
    # keyword = request.args.get('key')
    # if not keyword:
    #     return '请输入查询字符串'
    # reslut = get_title(keyword)
    # data = []
    # for item in reslut:
    #     del item['_source']['content']
    #     data.append(item['_source'])
    # return  render_template('index.html',reslut=data)


@app.route('/company')
def company():
    name = request.args.get('name')
    datas = []
    xsd, text = get_data(jieba.lcut(name))
    for i in range(len(xsd)):
        datas.append({
            'confidence': xsd[i],
            'text': text[i]
        })
    data = {
        'company': name,
        'discriminate':datas
    }
    # print()
    return Response(json.dumps(data,cls=MyEncoder),mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
