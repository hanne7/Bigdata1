import re

p = re.compile("\section")
m = p.findall("\section")
print(m)
m = p.findall(" ection")
print(m)

p = re.compile("\\section")
m = p.findall("\section")
print(m)

p = re.compile(r"section")
m = p.match("\section")
print(m)

p =re.compile(r"\\section")
m = p.match("\section")
print(m)