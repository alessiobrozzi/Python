import re

# encoding=utf8

# ex 1a: retunr string if first three characters are digits
x = raw_input('enter string: ')

y = x[0:3]

if(re.sub("[0-9][0-9][0-9]", "y", y) == 'y'):
    print y
# 1b: return all words in string that end with "ly"
x = raw_input('enter sring; ')

z = re.findall('[a-z]*ly', x)

for i in z:
    print i

# 1c : replaces all words startng in "wh" with "WH-word"

x = raw_input('enter string: ')

u = re.sub('wh[a-z]*', 'WH-word', x)

print u
