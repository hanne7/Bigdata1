import requests
from bs4 import BeautifulSoup

RANK = 100

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
html = req.text
parse = BeautifulSoup(html, 'html.parser')

titles = parse.find_all("div", {"class": "ellipsis rank01"})
songs = parse.find_all("div", {"class": "ellipsis rank02"})

title = []
song = []

for t in titles:
    title.append(t.find('a').text)

for s in songs:
    song.append(s.find('span', {"class": "checkEllipsis"}).text)

for i in range(RANK):
    print('%3d위: %s - %s' % (i + 1, title[i], song[i]))