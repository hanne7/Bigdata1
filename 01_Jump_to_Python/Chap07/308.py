import re

p = re.compile('aaa.bbb')
dest_str = '''aaa
bbb'''
m = p.match(dest_str)
print(m)

#p = re.compile('aaa.bbb', re.DOTALL)
p = re.compile('aaa.bbb', re.S)
m = p.match(dest_str)
print(m)

#p = re.compile('[a-z]+', re.I)
p = re.compile('[a-z]+', re.IGNORECASE)
m = p.match('python')
print(m)
m = p.match('Python')
print(m)
m = p.match('PYTHON')
print(m)


