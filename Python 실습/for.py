tuple = (1,2,3,4,5,6)

for i in tuple:
    print(i)

list = [(1,2),(3,4),(5,6)]
for(first, last) in list:
    print(first + last)

marks = [90,25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다. " %number)

#숫자 리스트를 자동으로 만들어주는 range함수
add = 0
for i in range(0,10):
    add += i

print(add)

#리스트를 내포하여 사용하기
a = [1,2,3,4]
result =[num*3 for num in a]
print(result)

result2 = [x*y for x in range(1,3) for y in range(1,4)]
print(result2)

for x in range(1,3):
    print("엑스는")
    print(x)
    for y in range(1,4):
        print("와이는")
        print (y)
        print("곱결과")
        print (x*y)