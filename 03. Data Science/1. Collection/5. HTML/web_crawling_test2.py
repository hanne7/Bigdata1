from bs4 import BeautifulSoup
from pandas import DataFrame
import urllib.request
import os

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
    dir_index = len(os.listdir('V2_bigdata'))
    if len(os.listdir('V2_bigdata')) == 0:
        dir_index = 1
except:
    dir_index = 1

try:
    if len(os.listdir('V2_bigdata')) == 1:
        file_index = len(os.listdir('V2_bigdata')) * len(os.listdir('V2_bigdata\\naver_ranking%d' % dir_index))
    elif len(os.listdir('V2_bigdata')) >= 2:
        file_index = (dir_index-1) * 3 + len(os.listdir('V2_bigdata\\naver_ranking%d' % dir_index))
    else:
        file_index = 1
except:
    file_index = 1

dir_name = 'V2_bigdata'
dir_name2 = '\\naver_ranking'

if not (os.path.isdir(dir_name)):
    os.makedirs(os.path.join(dir_name))

if len(os.listdir(dir_name)) == 0:
    os.makedirs(os.path.join(dir_name+dir_name2+str(dir_index)))

if len(os.listdir(dir_name+dir_name2+str(dir_index))) < 3:
    if os.path.isfile(dir_name+dir_name2+str(dir_index)+'\\movie%d.csv'%file_index):
        file_index += 1
        if os.path.isfile(dir_name + dir_name2 + str(dir_index) + '\\movie%d.csv' % file_index):
            file_index -=2
        rank_table.to_csv(dir_name+dir_name2+str(dir_index)+'\\movie%d.csv'%file_index, encoding='utf-8', mode='w', index=False)
    else:
        rank_table.to_csv(dir_name + dir_name2 + str(dir_index) + '\\movie%d.csv' % file_index, encoding='utf-8', mode='w', index=False)
elif len(os.listdir(dir_name+dir_name2+str(dir_index))) == 3:
    dir_index += 1
    os.makedirs(os.path.join(dir_name+dir_name2+str(dir_index)))
    if os.path.isfile(dir_name+dir_name2+str(dir_index)+'\\movie%d.csv'%file_index):
        file_index += 1
        rank_table.to_csv(dir_name+dir_name2+str(dir_index)+'\\movie%d.csv'%file_index, encoding='utf-8', mode='w', index=False)
    else:
        file_index += 1
        rank_table.to_csv(dir_name + dir_name2+str(dir_index)+ '\\movie%d.csv' % file_index, encoding='utf-8', mode='w', index=False)