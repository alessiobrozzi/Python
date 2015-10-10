#for every element in list print '* + fiorst two letters + whole element'

import re

# encoding=utf8

def checkPrefix(string, prefix):
    list = re.findall('[a-z]+', string)
    for i in list:
        x = '* '
        y = prefix
        whole = x + y + ' ' + i
        print whole

