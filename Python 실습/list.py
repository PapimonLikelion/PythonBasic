#리스트 실습 & 내장함수

li = [3,1,"기어코", 4, "떠나버린", 5, "사람아", 1]
li2 = [3,2,1,4,5]
li3 = ["기어코", "떠나버린", "사람아"]

#리스트의 길이를 구해주는 함수 : len(변수)
print(len(li))

#리스트 오름차순 정렬 : 변수.sort()
print(li2)
li2.sort()
print(li2)

print(li3)
li3.sort()
print(li3)

#리스트 내의 특정원소 반환 : 변수.index("원소명")
print(li.index("기어코"))

#리스트 내의 특정원소의 갯수 세기: 변수.count(요소)
print(li.count("기어"))

