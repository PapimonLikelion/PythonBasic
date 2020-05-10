treeHit=0
while (treeHit<10):
    treeHit = treeHit+1
    print("나무 %d번 찍었습니다." %treeHit)
    if(treeHit == 10):
        print("나무 넘어감")


treeHit2=0
while(1):
    treeHit2=treeHit2+1
    print("나무 %d번 찍었다" %treeHit2)
        
    if(treeHit2==20):
        break


coffee = 10
while True:
    money = int(input("돈을 넣어봐: "))
    if money == 300:
        print("커피드립니다")
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d와 커피입니다." %(money-300))
    else:
        print("돈을 주고 커피안줘")