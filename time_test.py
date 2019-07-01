#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re


def test_clock():
    time.sleep(2)           # sleep seconds
    time1 = time.clock()    # time diff from process start
    time.sleep(2)
    time2 = time.clock()    # time diff from last time.clock()
    print "time1:{0} time2:{1}".format(time1, time2)

# test_clock()

cur_time_second = time.time()
# print cur_time_second
cur_tuple_localtime = time.localtime(time.time())
# cur_tuple_localtime = time.localtime()    # convert current time in tuple
# print cur_tuple_localtime

# cur_tuple_gmtime = time.gmtime(time.time())
# cur_tuple_gmtime = time.gmtime()    # convert current time in tuple
# print cur_tuple_gmtime

# print time.ctime(cur_time_second)    # convert seconds time to ascii time
# print time.ctime()    # convert seconds time to ascii time
# print time.asctime(cur_tuple_localtime)    # convert tuple time to ascii time
# print time.asctime()    # convert current tuple time to ascii time


# format_time = time.strftime("%Y-%m-%d %H:%M:%S", cur_tuple_localtime)
# format_time = time.strftime("%Y-%m-%d %H:%M:%S")                          # current time
# print format_time

tuple_time = time.strptime("2015-03-15 22:44:15", "%Y-%m-%d %H:%M:%S")
print tuple_time








