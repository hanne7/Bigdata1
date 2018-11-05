from bs4 import BeautifulSoup
import urllib.request


news_link = 'https://news.naver.com'

html = urllib.request.urlopen('https://news.naver.com/main/ranking/popularDay.nhn')
soup = BeautifulSoup(html, 'html.parser')


tags = soup.findAll('ul', attrs={'class':'section_list_ranking'})

news_url = []
num = 0
for news in tags:
    with open('ranking_news%s.csv'%str(num+1), 'w', encoding='utf-8') as outfile:
        outfile.write(str(tags[num]))
        num+=1

num = 0
for news in tags:
    with open('ranking_news%s.csv'%str(num+1), 'r', encoding='utf-8') as readfile:
        a = readfile.readlines()
        del a[11]
        del a[0]
        for line in a:
            i = line.split('href="')
            j = i[1].split('" title')
            k = j[1].split('>')
            m = k[1].split('<')
            news_url.append(m[0] + '\n' + news_link + j[0].replace('&amp;', '&') + '\n')
    num+=1

politic_news = news_url[:10]
economic_news = news_url[10:20]
social_news = news_url[20:30]
living_news = news_url[30:40]
world_news = news_url[40:50]
IT_news = news_url[50:]

for i in living_news:
    print(i)


