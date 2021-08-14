#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://liam.page/2016/02/27/The-requests-library-in-Python/

import time
import sys
import getopt
import json
import requests


def print_info(response, para_dict):
    outfilename = "result_out.data"
    if 'file' in para_dict:
        outfilename = para_dict['file']

    outfile = open(outfilename, "w")
    json_obj = json.loads(response.text)
    json_str = json.dumps(json_obj, ensure_ascii=False)
    print(json_str)
    cat_num = 0
    if "cats" in json_obj:
        cats = json_obj["cats"]
        cat_num = len(cats)
        print("cats len:", cat_num)
        outfile.write("cat_num:" + str(cat_num) + "\n")
        outfile.write("title\t\t\tweight\n")
        for cat in cats:
            title = cat["title"]
            outfile.write(title + "\t\t\t")
            weight = cat["weight"]
            outfile.write(weight + "\n")
    outfile.write("\n")
    item_num = 0
    if 'items' in json_obj:
        items = json_obj['items']
        item_num = len(items)
        print("items len:", item_num)
        outfile.write("item_num:" + str(item_num) + "\n")
        count = 0
        outfile.write("number\t\t\tgoodsId\t\t\tscore\n")
        while count < len(items):
            outfile.write(
                str(count + 1) + "\t\t\t" + items[count]['goods_id'] + "\t\t\t" + str(items[count]['score']) + "\n")
            count += 1
    outfile.close()


# paras: type:dict
def get_result(paras):
    host = '192.168.16.111'
    port = 7861
    query = ''

    if 'host' in paras:
        host = paras['host']
    if 'port' in paras:
        port = int(paras['port'])
    if 'query' in paras:
        query = paras['query']

    url = "http://%s:%s/shard/recall" % (host, port)

    headers = {"Content-Type": "application/json;charset=UTF-8"}
    params = dict()

    params["query"] = query
    cur_time_ms = int(time.time() * 1000)
    reqId = str(cur_time_ms)
    params["reqId"] = reqId
    # cat = 21808 # 手机
    # predictCats = '[{"value":1,"key":21808}]'  # 手机
    # predictCats = '[{"value":0.9928878,"key":16270}]'   # 优酸乳
    userId = 96417343
    params["userId"] = userId
    ip = "58.247.129.10"
    params["ip"] = ip
    version = "beta"
    params["version"] = version
    sort = "_default"
    params["sort"] = sort
    # size=2000
    cateNumShow = 20
    params["cateNumShow"] = cateNumShow
    collectionName = "mainsearch"
    params["collectionName"] = collectionName
    shardName = "shard-2"
    params["shardName"] = shardName

    cat = ""
    abFlag = ""
    size = 2000
    params["size"] = size
    maxPrice = 999999900
    params["maxPrice"] = maxPrice

    # predictCats = '{}'
    predictCats = '[{"value":0.98778105,"key":15896}]'
    # abFlag="recall:keyword_vector;version:alpha;"
    # abFlag="weighting:goodmall;version:beta;"
    # abParams="search-a:0:0"


    response = requests.post(url, headers=headers, json=params)
    print("status_code:", response.status_code)
    if response.status_code != requests.codes.ok:
        exit(1)
    return response


# argv: para array
def parse_paras(argv):
    paras = {}
    try:
        opts, args = getopt.getopt(argv, "h:p:q:f:", ["host=", "port=", "query=", "file="])
        # args一般是无用的
    except getopt.GetoptError:
        print('Param Error')
        exit(1)
    for opt, arg in opts:
        if opt in ('-h', '--host'):
            paras['host'] = arg
        if opt in ('-p', '--port'):
            paras['port'] = arg
        if opt in ('-q', '--query'):
            paras['query'] = arg
        if opt in ('-f', '--file'):
            paras['file'] = arg
    return paras


def main():
    para_dict = parse_paras(sys.argv[1:])
    start = time.time_ns()
    response = get_result(para_dict)
    print_info(response, para_dict)
    end = time.time_ns()
    diff_time = (end - start) / 1000000
    print("diff_time_ms:", diff_time, "ms")


# 例子
# -h 199.128.0.1，-p 7860, -q = 中国，
if __name__ == '__main__':
    main()




