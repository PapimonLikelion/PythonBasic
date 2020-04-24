for waiting_no in [0,1,2,3,4]:
    print("대기번호: {}".format(waiting_no))

print("")

for waiting in range(1,6):
    print("대기번호: {}".format(waiting))

starbucks = ["아이언맨", "토르", "그루트"]
for cust in starbucks:
    print("{%s} 커피나왔습니다" %cust)

#list에서의 활용
students=[1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["sdfkj","dsfsdjflksjf","oeriwuerioweruoweiruweoir"]
students = [i.upper() for i in students]
print(students)
students = [len(i) for i in students] #이렇게 하면 성격이 아예 int로 바뀐것이야 형변환도 고려해 줘야해
print(students)