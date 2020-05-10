#if문
#if(조건):

#ex1
#85점이상 Pass, else fail
score= int(input("점수? : "))
if(score>=85):
    print("PASS")
else:
    print("FAIL")

#ex2

activity = input("너동아리 뭐해? :")
if(activity == "멋사"):
    print("너도??")
else: 
    print("멋사 ㄱ")

#ex3
money = int(input("돈 얼마있냐? :"))
if(money > 50000):
    print("아웃백 ㄱ")
elif(money<50000 and money>30000):
    print("복계탕 ㄱ")
elif(money<30000 and money>10000):
    print("짱깨 ㄱ")
else:
    print("학식 ㄱ")