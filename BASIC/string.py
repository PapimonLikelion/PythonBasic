sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬 ㅈ밥"
print(sentence2)
sentence3 = """
파이썬
아주 
쉽다
"""
print(sentence3)

#SLICING
YS = "970610-1040433"
print("성별: ", YS[7])
print("연도: ",YS[0:2])
print("월: ", YS[2:4])
print("일: ", YS[4:6])
print("생년월일: ", YS[:6])
print("번호: ", YS[7:])
print("뒤부터: ", YS[-7:], "맨뒤에서 7번째부터 끝까지")

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index('n', index+1) #찾은 인덱스 부터 또 찾아 ... 그니까 2번쨰로 n이 어디에있냐는겨
print(index)

print(python.find("n"))
print(python.find("JAVA")) #없으면 -1
# print(python.index("JAVA")) #이건 에러여
print(python.count('n'))