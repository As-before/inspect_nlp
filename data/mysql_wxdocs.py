# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 15:05
# @Author  : YuDong.Pang

import pymysql

# 数据库配置字典
mysql_config = {
    "host": "~",
    "user": "sql1",
    "password": "~",
    "database": "~"
}


def select_wxdocs_data():
    '''
    查询当天指定公众号名称的所有数据
    :param name: 公众号名称
    :return: 元组类型
    '''
    # 获取当天时间日期
    db = pymysql.connect(**mysql_config)
    cursor = db.cursor()
    # 查询语句
    sql = "select wxcontent,id from wxdocs limit 0,100"
    r = cursor.execute(sql)  # 返回值r为受影响的行数
    ret = cursor.fetchall()
    if ret is None:
        return []
    else:
        return ret
