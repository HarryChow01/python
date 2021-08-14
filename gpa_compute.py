#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def map_4_1(mark):
    if mark >= 90:
        return 4.0
    elif mark >= 80:
        return 3.0            
    elif mark >= 70:
        return 2.0
    elif mark >= 60:
        return 1.0
    else:
        return 0


def map_4_2(mark):
    if mark >= 90:
        return 4.0
    elif mark >= 87:
        return 3.7
    elif mark >= 83:
        return 3.3
    elif mark >= 80:
        return 3.0            
    elif mark >= 77:
        return 2.7
    elif mark >= 73:
        return 2.3
    elif mark >= 70:
        return 2.0
    elif mark >= 60:
        return 1.0
    else:
        return 0


def map_4_3(mark):
    if mark >= 85:
        return 4.0
    elif mark >= 75:
        return 3.0
    elif mark >= 60:
        return 2.0
    else:
        return 0


def compute_gpa(infile_name, gpa_type):
    infile = open(infile_name)
    
    total_mark = 0
    total_credit = 0
    
    for line in infile:
        credit = float(line.split()[0])
        cur_mark = int(line.split()[1])
        mark = 0
        if gpa_type == 0:
            mark = cur_mark
        elif gpa_type == 1:
            mark = map_4_1(cur_mark)
        elif gpa_type == 2:
            mark = map_4_2(cur_mark)
        elif gpa_type == 3:
            mark = map_4_3(cur_mark)

        total_credit += credit
        total_mark += mark * credit
        
    gpa = total_mark / total_credit
    print("gpa = %f" % gpa)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please input : %s score_file type" % (sys.argv[0]))
        exit(1)
    gpa_type = int(sys.argv[2])
    if gpa_type != 0 and gpa_type != 1 and gpa_type != 2 and gpa_type != 3:
        print("type error")
        exit(1)
    compute_gpa(sys.argv[1], gpa_type)

