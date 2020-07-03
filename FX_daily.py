#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None





def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='FXM',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_12 = "%s," *12
        cursor.executemany('insert into FX_mon ({0}) values ({1})'.format(FX_c,f_12[:-1]), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    big_list = []
    FX_c = 'USDJPY,EURJPY,AUDJPY,GBPJPY,NZDJPY,CADJPY,CHFJPY,ZARJPY,CNHJPY,EURUSD,GBPUSD,AUDUSD'
    f_FX =FX_c.split(",")
    for code in f_FX:
        url = 'https://info.finance.yahoo.co.jp/fx/detail/?code={0}=FX'.format(code)

        html = call_page(url)
        patt = re.compile('<dd id="{0}_detail_ask">(.*?)<span class="large">(.*?)</span>(.*?)</dd></dl>'.format(code), re.S)
        items = re.findall(patt, html)

        for it in items:
            f = "".join(list(it))
            big_list.append(f)


        print(big_list)
        print(url)
    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    print(ff_l)
    insertDB(ff_l)






# create table FX_mon (id int not null primary key auto_increment, USDJPY float ,EURJPY float ,AUDJPY float ,GBPJPY float ,NZDJPY float ,CADJPY float ,CHFJPY float ,ZARJPY float ,CNHJPY float ,EURUSD float ,GBPUSD float ,AUDUSD float , LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table FX_mon;


# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py