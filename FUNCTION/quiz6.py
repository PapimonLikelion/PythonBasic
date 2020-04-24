def std_weight(height, gender):
    if(gender=="여자"):
        return (height/100)**2*21
    else:
        return (height/100)**2*22

height = int(input("키: "))
gender = input("성별: ")
weight = round(std_weight(height, gender),2)

if(gender=="남자"):
    print("키 {0}cm 남자의 표준 체중은 {1}kg입니다. ".format(height, weight))   
else:
    print("키 {0}cm 여자의 표준 체중은 {1}kg입니다. ".format(height, weight))   