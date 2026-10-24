#! python3
# regex validation

import re

text = ('''abcdefgh''')

# search = ^.{3}%s
letter = 'd'
number = 3
text = text.split('/n')

for bip in text:
    # search
    searching = re.compile(r'^.{%s}%s' % (number, letter))
    found = searching.search(bip)
    # print results
    if found != None:
        print(found)
    else:
        print('Found nothing in %s.' % (bip))
    