cust = "토르"
index = 5
while index>=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(cust, index))
    index-=1
    if index==0:
        print("커피는 폐기처분 되었다")

cust = "아이언맨"

index=1
while True:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(cust, index))
    index+=1
    if index == 10:
        break

absent = [2,5]
nobook = [7]
for student in range(1,11):
    if student in absent:
        continue
    if student in nobook:
        print("뭐라고?", student,"열로와")
        break
    print("{0}, 책을 읽어봐".format(student))