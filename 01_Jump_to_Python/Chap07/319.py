import re

p = re.compile(r"(\b\w+)\s+\1")
#p = re.compile(r"(\b\w+)\s+\2")
print(p.search("Paris in the the spring").group())
print(p.findall("Paris in the the spring kkk kkk OK"))