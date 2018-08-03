import urllib.request
import datetime
import json
import time
import os

access_key="VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D"
repo_base_name="BigData_Repo"
dir_delimeter='/'
depth_level2_dir="weather_info"
file_limit=3

def make_base_dir():
    os.mkdir('.'+dir_delimeter+repo_base_name)

def make_d2_dir(dir_num):
    os.mkdir('.'+dir_delimeter+repo_base_name+'\\'+depth_level2_dir+dir_num)

def directory_num():
    #마지막 디렉토리의 번호를 구한다.
    #만약 마지막 디렉토리안에 파일 갯수가 임계치에 다다르면 새로운 디렉토리를 생성한다.
    dir_num=len(os.listdir('.'+dir_delimeter+repo_base_name))
    if len(os.listdir('.'+dir_delimeter+repo_base_name+dir_delimeter+depth_level2_dir+str(dir_num))) == file_limit:
        dir_num+=1
        make_d2_dir(str(dir_num))
    return str(dir_num)

def get_Request_URL(url):                 ## (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)     ## request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):       ## (1) 기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=100"

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)


def Make_Weather_Json(day_time):     ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate': prn_data.get('baseDate'),
                               'baseTime': prn_data.get('baseTime'),
                               'category': prn_data.get('category'),
                               'fcstDate': prn_data.get('fcstDate'),
                               'fcstTime': prn_data.get('fcstTime'),
                               'fcstValue': prn_data.get('fcstValue'),
                               'nx': prn_data.get('nx'),
                               'ny': prn_data.get('ny')})
    # rank_table.to_csv(
    #     '.' + dir_delimeter + repo_base_name + dir_delimeter + depth_level2_dir + directory_num() + dir_delimeter + file_name + '.' + csv,
    #     encoding='utf8', mode='w', index=True)
    # with open('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd,day_time), 'w', encoding='utf8') as outfile:
    with open('.%s%s%s%s%s%s동구_신암동_초단기예보조회_%s%s%s.json' \
              % (dir_delimeter,repo_base_name,dir_delimeter,depth_level2_dir,\
                 directory_num(),dir_delimeter,yyyymmdd,day_time,day_sec), \
              'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n' % (yyyymmdd, day_time))

def get_Realtime_Weather_Info():        ## (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59:      ## 실시간 업데이트가 있는지 없는지 확인,, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:        ## 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전껄로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int-30) # 정확히 30분을 뺀다.
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)      ## 시간이 한 자리 수일 때 930 되는 것을 0930으로 바꿔 줌

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    return day_min_int

json_weather_result = []
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
day_sec = time.strftime("%S")
x_coodinate = "89"
y_coodinate = "91"

if not os.path.exists('.'+dir_delimeter+repo_base_name) :
    make_base_dir()
if not os.path.exists('.'+dir_delimeter+repo_base_name+dir_delimeter+depth_level2_dir+'1'):
    make_d2_dir('1')

get_Realtime_Weather_Info()


