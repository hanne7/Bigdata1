import urllib.request
import datetime
import json
import re
from operator import itemgetter

access_key = "3dXwHlR2x4duU5goEFsQ4tx2MsbpB%2FND4segfhRTBVcykfUUQJB%2BAer3KGvpSTilj1xJetgS52geOw4qwIpR2g%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s"%(datetime.datetime.now(), url))
        return None

# [CODE 1]
def getNatVisitor(yyyymm, nat_cd, ed_cd):
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd

    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    jsonResult = []
# 중국:112/ 일본:130/ 미국:275

    f = open('national_code_selected.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    nations = []
    for i in lines:
        nations.append(re.findall('\d+', i)[0])
    for nation in nations:
        national_code = nation
        ed_cd = "E"
        yyyymm = '201712'
        jsonData = getNatVisitor(yyyymm, national_code, ed_cd)

        if(jsonData['response']['header']['resultMsg'] == 'OK'):
            krName = jsonData['response']['body']['items']['item']['natKorNm']
            krName = krName.replace(' ','')
            iTotalVisit = jsonData['response']['body']['items']['item']['num']
            print('%s_%s:%s'%(krName, yyyymm, iTotalVisit))
            jsonResult.append([krName, iTotalVisit])

        jsonResult.sort(key=itemgetter(1), reverse=True)

    with open('test.json', 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()