import re
p=re.compile('[a-z]')
m = p.match('kill')
print(m)

p=re.compile('[a-z]')
m = p.match('1st')
print(m)

p=re.compile('[a-z]')
m = p.match('Orange')
print(m)

p=re.compile('[a-zA-Z]')
m = p.match('Kill')
print(m)

p=re.compile('[a-zA-Z]')
m = p.match('Orange')
print(m)

p=re.compile('[0-9]')
m = p.match('0')
print(m)

p=re.compile('[0-9]')
m = p.match('-1')
print(m)

p=re.compile('[A-Z][0-9]')
m = p.match('K9')
print(m)