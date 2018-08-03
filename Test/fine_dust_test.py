import urllib.request
import datetime
import json

access_key = "4ruU7ayu0r%2BGctDhbc6L3IruWayh2oiaMDsR%2Fo8iuhpo2qZTPwKyhrKj1EvfIMqssGehRSCfQlQw4uO%2BR6bSXg%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(), url))
        return  None

def getFinedust(sidoName):
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    parameters = "?sidoName=" + sidoName
    parameters += "&pageNo=1&numOfRows=15&ver=1.3"
    parameters += "&_returnType=json&serviceKey=" + access_key
    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return  None
    else:
        return json.loads(retData)

def main():
    jsonResult = []
    now = datetime.datetime.now()
    sidoName = '%EB%8C%80%EA%B5%AC'  # 대구

    jsonData = getFinedust(sidoName)
    for i in jsonData['list']:
        if i['stationName'] == '신암동':
            jsonResult.append(i)

    with open('finedust%s.json'%now.strftime('%Y%m%d%H%M'), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()