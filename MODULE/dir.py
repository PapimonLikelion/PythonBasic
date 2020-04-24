#내장함수 찾기
print(dir())
import random
print(dir())

lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))

#외장함수
#윈도우 dir
import glob
print(glob.glob("*.py"))

import os
print(os.getcwd())
folder = "sample"
if os.path.exists(folder):
    print("이미 존재하는 폴더")
    os.rmdir(folder)
    print("삭제완료")
else:
    os.makedirs(folder)
    print(folder, "생성완료")

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())
today = datetime.date.today()
hundred_days_later =  datetime.timedelta(days=100)
print("100일 후는 ", today + hundred_days_later)