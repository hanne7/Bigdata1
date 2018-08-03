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

def getForecast(base_date, base_time, nx, ny):
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + base_date
    parameters += "&base_time=" + base_time
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += '&numOfRows=100'

    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return  None
    else:
        return  json.loads(retData)

def main():
    jsonResult = []
    now = datetime.datetime.now()
    base_date = now.strftime('%Y%m%d')
    if int(now.strftime('%M')) >= 30 and int(now.strftime('%M')) <= 59:
        base_time = now.strftime('%H%M')
    else:
        hour = int(now.strftime('%H')) - 1
        min = int(now.strftime('%M')) - 30 + 60
        base_time = str(hour) + str(min)
    nx = '89'
    ny = '91'

    jsonData = getForecast(base_date, base_time, nx, ny)
    if(jsonData['response']['header']['resultMsg'] == 'OK'):
        for i in jsonData['response']['body']['items']['item']:
            jsonResult.append(i)


    with open('forecast%s.json'%now.strftime('%Y%m%d%H%M'), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()