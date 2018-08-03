import re

p = re.compile('hello\s\w')
dest_str = 'hello my hello world! hello!'
m = p.match(dest_str)
print(m)
m=p.findall(dest_str)
print(m)

print()
print("^사용후")
p = re.compile('^hello\s\w')
dest_str = 'hello my hello world! hello!'
m = p.match(dest_str)
print(m)
m=p.findall(dest_str)
print(m)

