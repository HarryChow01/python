#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re


#pattern = re.compile(r"\w*")
pattern = re.compile("[a-zA-Z]+")       # "aCc 123"
#pattern = re.compile("[0-9]*")       # "123"

#pattern = re.compile(" *")       # "    "
#pattern = re.compile(r"\s*")       # "    "
#pattern = re.compile(r"\S*")       # "abc123"

#pattern = re.compile(r"\d*")       # "123"
#pattern = re.compile("\\d*")       # "123"
#pattern = re.compile("\\D*")       # "abc"
#pattern = re.compile(r"\D*")       # "abc"

#pattern = re.compile(r"\w*")       # "acB123"
#pattern = re.compile("\\w*")       # "123"
#pattern = re.compile(r"\W*")       # "    "
#pattern = re.compile("\\W*")       # "    "

#pattern = re.compile("\\*")       # "/"
#pattern = re.compile("[a-z]*")

#pattern = re.compile(r"\d{4}")       # "34214"
#pattern = re.compile(r"\d{4,6}")       # "34214","3421","342142", "34214333"


text_str = "ABC123abc333"
# pattern = re.compile("[a-zA-Z]+")       #
pattern = re.compile("[a-zA-Z]*")       #
#match = pattern.match(text_str)
match = pattern.findall(text_str)
print match

w1 = r"[a-zA-Z]+"
#m1 = re.search(w1, text_str)
#m1 = match.findall(w1, text_str)







