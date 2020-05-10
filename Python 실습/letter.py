#문자열에 번호를 붙여 효울적관리
#INDEX 방법!
#"내이름은 민철이야"
# 0 1 2 3 4 5 6 7 8
# -7 ~~~~~~~~~~~ -1

#SLICING 방법!
#index1부터 ~ index2 !!!!전까지!!!
#str="hello"
#str[0:2] ... 0<= index <2
#str[0:2]=="he"

string = str(input("이름이 뭐야? : "))
print(string)
print(string + "의 성은 : " + string[0])

string2 = str(input("외국인 너 이름뭐야? : "))
print(string2)
print("너는 이름이 너무 기니까 3글자로 줄일게 --" , string2[0:3])