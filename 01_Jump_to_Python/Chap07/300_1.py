import re

p = re.compile('a.b')
m = p.match('aab')
print(m)

p = re.compile('a.b')
m = p.match('a0b')
print(m)

p = re.compile('a.b')
m = p.match('abc')
print(m)

p = re.compile('ca*t')
m = p.match('ct')
print(m)

p = re.compile('ca*t')
m = p.match('cat')
print(m)
p = re.compile('ca*t')
m = p.match('caaaat')
print(m)

p = re.compile('ca+t')
m = p.match('ct')
print(m)

p = re.compile('ca+t')
m = p.match('cat')
print(m)

p = re.compile('ca+t')
m = p.match('caaaaaaaaat')
print(m)

p = re.compile('ca?t')
m = p.match('caat')
print(m)