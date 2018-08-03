import re

p = re.compile(".*[.].*$")
m = p.search("google.bat")
print(m.group())

print()
p = re.compile(".*[.][^b].*$")
m = p.search("google.bat")
print(m)

m = p.search("google.com")
print(m.group())

m = p.search("google.bar")
print(m)

print()
p = re.compile(".*[.]([^b]..|.[^a].|..[^t])$")

print(p.search("google.bat"))
print(p.search("google.com").group())
print(p.search("google.bar").group())
print(p.search("google.cf"))

print()
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
print(p.search("google.bat"))
print(p.search("google.cf").group())

print()
#p = re.compile(".*[.](?!bat$).*$")
p = re.compile(".*[.](?!bat$|exe$).*$")
print(p.search("google.bat"))
print(p.search("google.cf").group())
print(p.search("google.bar").group())
print(p.search("google.exe"))

