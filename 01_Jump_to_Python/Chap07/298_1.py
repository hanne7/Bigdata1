import re
p = re.compile('[abc]')
m = p.match('a')
print(m)
m = p.match("before")
print(m)
m = p.match('dude')
print(m)
m = p.match('dad')
print(m)

print()

p = re.compile('[abc][abc]')
m = p.match('dad')
print(m)
p = re.compile('d[abc]')
m = p.match('dad')
print(m)

print()
p = re.compile('[aekj][i][e]')
m = p.match('cie')
print(m)