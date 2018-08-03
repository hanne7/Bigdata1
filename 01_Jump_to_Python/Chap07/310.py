import re

dest_str = """python one python debug
life is too short
python two
you need python skill
python three
"""

p = re.compile("^python\s\w+")
m = p.findall(dest_str)
print(m)

print()
p = re.compile("^python\s\w+", re.DOTALL)
m = p.findall(dest_str)
print(m)

print()
p = re.compile("^python\s\w+", re.MULTILINE)
m = p.findall(dest_str)
print(m)
