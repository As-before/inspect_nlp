# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 15:07
# @Author  : YuDong.Pang
import pymysql

# 数据库配置字典
config = {
    "host": "~",
    "user": "sql1",
    "password": "~",
    "database": "test"
}


def select_xfdata():
    '''
    查询当天指定公众号名称的所有数据
    :param name: 公众号名称
    :return: 元组类型
    '''
    # 获取当天时间日期
    db = pymysql.connect(**config)
    cursor = db.cursor()
    # 查询语句
    sql = "select content,id,url from splider_xzcf limit 0,100"
    r = cursor.execute(sql)  # 返回值r为受影响的行数
    ret = cursor.fetchall()
    if ret is None:
        return []
    else:
        return ret
