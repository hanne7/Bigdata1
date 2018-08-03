from bs4 import BeautifulSoup
from pandas import DataFrame
import urllib.request
import os
import time

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})
up_downs =  soup.findAll('img', attrs={'class':'arrow'})
ranks = soup.findAll('img', attrs={'width':'14'})
ranges = soup.findAll('td', attrs={'class':'range ac'})


result = []
i = 0
while i < len(ranks):
    result.append([int(ranks[i]['alt'])] + [tags[i].a['title']] + [ranges[i].string + ', ' + up_downs[i]['alt']])
    i += 1

rank_table = DataFrame(result, columns=('rank','name','range'))



try:
    dir_index = len(os.listdir('V3_bigdata'))
    if len(os.listdir('V3_bigdata')) == 0:
        dir_index = 1
except:
    dir_index = 1

dir_name = 'V3_bigdata'
dir_name2 = '\\naver_ranking'

now = time.localtime()
'%04d-%02d-%02d_%02d%02d%02d'%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

if not (os.path.isdir(dir_name)):
    os.makedirs(os.path.join(dir_name))

if len(os.listdir(dir_name)) == 0:
    os.makedirs(os.path.join(dir_name+dir_name2+str(dir_index)))

if len(os.listdir(dir_name+dir_name2+str(dir_index))) < 3:
    rank_table.to_csv(dir_name + dir_name2 + str(dir_index) + '\\%04d-%02d-%02d_%02d%02d%02d'%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec), encoding='utf-8', mode='w', index=False)
elif len(os.listdir(dir_name+dir_name2+str(dir_index))) == 3:
    dir_index += 1
    os.makedirs(os.path.join(dir_name+dir_name2+str(dir_index)))
    rank_table.to_csv(dir_name+dir_name2+str(dir_index)+'\\%04d-%02d-%02d_%02d%02d%02d'%(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec), encoding='utf-8', mode='w', index=False)
