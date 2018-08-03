import re

mails = """park@naver.com
kim@daum.net
lee@myhome.co.kr
"""

#p = re.compile('.*[@].*[.].*$', re.MULTILINE)
p = re.compile('.*[@].*[.](?:com$|net$)', re.MULTILINE)
print(p.findall(mails))