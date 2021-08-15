#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tushare as ts

token = 'a0f36f2e8026f111304d55d9c561421c00cac4c9702d39d8a44a5d32'


def get_stock():
    pro = ts.pro_api(token)
    data = pro.stock_basic()
    num = len(data)
    print(num)
    for i in range(num):
        row = data.iloc[i].values.tolist()
        print(row)
        break


if __name__ == '__main__':
    get_stock()
