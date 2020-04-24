print("Python", "Java", sep=",", end=" ")
print("무엇이 더 재미난가요?")

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재미난가요?")

scores = {"수학": 0, "영어" : 50, "코딩": 100}
for subject, jumsoo in scores.items():
    print(subject.ljust(6), str(jumsoo).rjust(4), sep=":")

#zero fill
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# answer = input("아무값이나 입력 ㄱ :")
# print("넌", answer)

#오른쪽 정렬
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_>+10}".format(500))
#왼쪽 정렬
print("{0: <10}".format(500))
print("{0: <+10}".format(500))
print("{0: <+10}".format(-500))
print("{0:_<10}".format(500))
#3자리 마다 콤마
print("{0:,}".format(100000000000000000000))
print("{0:+,}".format(100000000000000000000))
print("{0:+,}".format(-100000000000000000000))
#3자리마다 콤마 찍어주기 30 자리수확보 나머지 ^로채우기
print("{0:^>+50,}".format(100000000000000000000))

#소수점 
print("{0:f}".format(5/3))
#소수점 둘째 까지출력
print("{0:.2f}".format(5/3))