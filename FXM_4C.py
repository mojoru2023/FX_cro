
# 放弃vba,直接上python

# -*- coding: utf-8 -*-

# 读取页面文本
# 按照标题，保存整个文本


import csv
import datetime
import numpy as np


import os
import re
import time
import sys

type = sys.getfilesystemencoding()
import pymysql
import xlrd






def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('FXM.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile


# xlsx---list_url----单页url
def get_allURL():

    lpath = os.getcwd()
    for item in ["FXM.xlsx"]:

        excelFile = '{0}\\{1}'.format(lpath,item)
        full_items = read_xlrd(excelFile=excelFile)


        #2---362
        for num in range(2,len(full_items[0])-1):
            _list= []

            for item in full_items:

                _list.append((item[num]))
            operate_list.append(_list)







if __name__ == '__main__':
    operate_list = []
    f_lst = []
    last_max_min_ = []
    headers=["js_industryDT","last_","max_","_min","_stdev"]

    get_allURL()
    for a in operate_list:
        f_1_0 = a[1:][0]
        for i in a[1:]:
            last_max_min_.append(round((i - f_1_0) / f_1_0, 4))
        stdev = last_max_min_[-100:]
        arr_std = np.std(stdev, ddof=1)

        _last = last_max_min_[-1]
        _max = max(last_max_min_)
        _min = min(last_max_min_)
        f_lst.append((a[0], _last, _max, _min, round(arr_std, 6)))
    writerDt_csv(headers,f_lst)
    print(f_lst)



