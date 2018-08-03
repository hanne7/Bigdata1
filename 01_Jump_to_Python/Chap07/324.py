import re
p = re.compile("(blue|white|red)")
print(p.sub('color', 'blue socks and red shoes'))

print(p.sub('color', 'blue socks and red shoes', count=1))
print()

print(p.subn('color', 'blue socks and red shoes'))
print()

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

print()

def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
