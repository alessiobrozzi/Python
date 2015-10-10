#for every element in list print '* + fiorst two letters + whole element'

import re

# encoding=utf8

list = ['how', 'why', 'however', 'where', 'never']

for i in list:
    x = '* '
    y = i[0:2]
    whole = x + y + ' ' + i
    print whole

for i in list:
    x = ' '
    y = i[0:2]
    whole = y + ' ' + i
    if (y == 'wh'):
        x = '* '
    else:
        x = '- '
    whole = x + whole
    print whole
