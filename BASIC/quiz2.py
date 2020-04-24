from random import randrange
date = randrange(1,29)
while(date != 3 | date !=2 | date != 1):
    date = randrange(1,29)

print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")