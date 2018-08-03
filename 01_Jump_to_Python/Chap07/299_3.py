import re

p = re.compile('[\d]')
m = p.match('7')
print(m)

p = re.compile('[\D]')
m = p.match('b')
print(m)

p = re.compile('[\s]')
m = p.match(' ')
print(m)

p = re.compile('[\S]')
m = p.match('a')
print(m)

p = re.compile('[\w]')
m = p.match('7')
print(m)

p = re.compile('[\w]')
m = p.match('a')
print(m)

p = re.compile('[\W]')
m = p.match('!')
print(m)

p = re.compile('[\W]')
m = p.match(' ')
print(m)

p = re.compile('[\d][\w][\w][\W]')
m = p.match('1st!')
print(m)