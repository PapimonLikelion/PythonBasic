weather = input("날씨:")
if weather == "비" or weather == "눈":
    print("우산우산")
elif weather == "미세":
    print("마스크")
else:
    print("출발")

temp = int(input("기온:"))
if 30<=temp:
    print("더워")
elif (10<= temp <30):
    print("ㄱㅊ")
else:
    print("COLD")