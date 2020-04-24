from random import *
customer = 0
yes = 0
for i in range (1,51):
    #customer 난수 생성
    customer = randint(1,50)
    if( 5<= customer <= 15):
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, customer))
        yes+=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, customer))

print("총 탑승승객 :",yes,"분")
        