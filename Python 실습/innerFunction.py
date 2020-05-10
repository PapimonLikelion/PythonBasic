#문자열(내장함수)

# 덧셈
str = "멋쟁이 사자,처럼은 "
str2 = "좋은 동아리 입니다"
print ((str+str2))
print(str[0])
print(str[0:4])

#문자열의 길이 구해주는 내장함수 : len(문자열 변수)
print(len(str))

#특정문자 등장횟수 : 문자열 변수.count("특정문자")
print(str.count("사"))

#문자열을 특정한 기준으로 나눠줌 : 문자열 변수.split()
print(str.split()) #띄어쓰기 기준으로 나눠서 리스트반환
print(str.split(',')) # , 기준으로 나눠서 리스트반환

#해당 글자가 몇번쨰 인덱스인가? : 문자열  변수.find('문자') , 문자열 변수.index('문자')
print(str.find('사'))
print(str.index('자'))