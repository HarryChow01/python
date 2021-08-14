#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import struct

goodsid2docid = {}
docid2goodsid = {}


def get_goods_id(infilename, outfilename, outfilename2):
    fsize = os.path.getsize(infilename)
    print("fsize:", fsize)
    fin = open(infilename, "rb")

    pos = fin.tell()

    while pos < fsize:
        # print("pos:", pos)
        len1, = struct.unpack('>h', fin.read(2))
        # print("len:", len1)
        format = "%ds" % len1
        str_id, = struct.unpack(format, fin.read(len1))
        str_id = str_id.decode()
        # print("len1:", len1, ", str_id:", str_id)
        fields = str_id.strip().split('#')
        if len(fields) != 2:
            continue

        goods_id = int(fields[0])
        doc_id = int(fields[1])
        # print("goods_id:", goods_id, ", doc_id:", doc_id)
        goodsid2docid[goods_id] = doc_id
        docid2goodsid[doc_id] = goods_id

        pos = fin.tell()

    fin.close()
    print("goodsid2docid size:", len(goodsid2docid))
    print("docid2goodsid size:", len(docid2goodsid))

    outfile = open(outfilename, "w")
    items = sorted(goodsid2docid.items(), key=lambda item: item[0])
    for item in items:
        outfile.write(str(item[0]) + "\t" + str(item[1]) + "\n")
    outfile.close()

    outfile2 = open(outfilename2, "w")
    items = sorted(docid2goodsid.items(), key=lambda item: item[0])
    for item in items:
        outfile2.write(str(item[0]) + "\t" + str(item[1]) + "\n")
    outfile2.close()


if __name__ == '__main__':
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    outfilename2 = sys.argv[3]
    get_goods_id(infilename, outfilename, outfilename2)
