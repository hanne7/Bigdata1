import urllib.request
import datetime
import json
import time
import os

access_key=''
repo_base_name='BigData_Repo'
dir_delimeter = '/'
depth_level2_dir='weather_info'
file_limit=3

def make_base_dir():
    os.mkdir('.' + dir_delimeter + repo_base_name)

def make_d2_dir(dir_num):
    os.mkdir('.' + dir_delimeter + repo_base_name + '')

