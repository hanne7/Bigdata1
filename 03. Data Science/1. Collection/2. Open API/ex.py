import json
import operator

with open("이명박_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)

inaccurate = 0
domains = []
print("데이터 분석을 시작합니다..")
i = 0
while i < len(jsonResult):
    try:
        domain_list = jsonResult[i].get("org_link").split("/")
        domains.append(domain_list[2])
    except:
        print("'org_link'가 없는 기사를 발견했습니다.")
        inaccurate += 1
    i += 1

domain_count = {}
for i in domains:
    try:
        domain_count[i] = domain_count[i] + 1
    except:
        domain_count[i] = 1

set_domains = set(domains)

print("네이버 검색 빅데이터 분석")
print("검색어 : 이명박")
print("전체 도메인 수 : %d"%len(set_domains))
print("전체 건수: %d"%len(jsonResult))
print("부정확한 데이터수 : %s"%inaccurate)
print()
print("- 도메인 별 뉴스 기사 분석")
sorted_list = sorted(domain_count.items(), key=operator.itemgetter(1), reverse=True)
for i in sorted_list:
    print(">> %s : %s건"%(i[0],i[1]))