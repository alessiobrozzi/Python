#for every element in list print '* + fiorst two letters + whole element'

import re

# encoding=utf8

def checkPrefix(list, prefix):
    for i in list:
        x = '* '
        y = prefix
        whole = x + y + ' ' + i
        print whole

inp = raw_input('enter string: ')
pref = raw_input('enter prefix: ')

lista = re.findall('[a-z]+', inp)

checkPrefix(lista, pref)
