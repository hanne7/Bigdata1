import urllib.request
import datetime
import json
import time
import os

access_key='VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D'
repo_base_name = "BigData_Repo"
dir_delimeter = "/"
depth_level2_dir = "weather_info"
file_limit = 3

def make_base_dir():
    os.mkdir('.' + dir_delimeter + repo_base_name)

def make_d2_dir(dir_num):
    os.mkdir('.' + dir_delimeter + repo_base_name + dir_delimeter + depth_level2_dir + dir_num)

def directory_num():
    dir_num = len(os.listdir('.' + dir_delimeter + repo_base_name))
    if len(os.listdir('.' + dir_delimeter + repo_base_name + dir_delimeter + depth_level2_dir + str(dir_num))) == file_limit:
        dir_num+=1
        make_d2_dir(str(dir_num))
    return  str(dir_num)

def get_Request_URL(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success'%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s'%(datetime.datetime.now(), url))
        return None

def get_Weather_URL(day_time):
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

def Make_Weather_Json(day_time):
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append(prn_data)

    with open('.%s%s%s%s%s%s동구_신암동_초단기예보조회_%s%s%s.json' \
              % (dir_delimeter, repo_base_name, dir_delimeter, depth_level2_dir, \
                 directory_num(), dir_delimeter, yyyymmdd, day_time, day_sec), \
              'w', encoding='utf8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json SAVED\n'%(yyyymmdd, day_time))

def get_Realtime_Weather_Info():
    day_min_int = int(day_min)
    if 30 < day_min_int <=59:
        day_time = time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int - 1
        revised_min = 60 + (day_min_int - 30)
        day_time = '{0:0>2}'.format(day_hour_int) + str(revised_min)

        print('\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n'.center(30))
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

if not os.path.exists('.' + dir_delimeter + repo_base_name):
    make_base_dir()
if not os.path.exists('.' + dir_delimeter + repo_base_name + dir_delimeter + depth_level2_dir + '1'):
    make_d2_dir('1')

get_Realtime_Weather_Info()