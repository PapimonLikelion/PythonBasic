cust = "이동기님"
index = 5


while index>=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(cust, index))
    index-=1
    if index==0:
        print("커피는 폐기처분 되었다")
