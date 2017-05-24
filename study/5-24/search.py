#!/usr/bin/env python
#-*-coding:utf-8-*-
import re
m = re.search('(?<=abc)def','abcdefg')
print m.group(0)
