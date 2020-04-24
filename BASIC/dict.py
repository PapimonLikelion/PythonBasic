cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3, "사용가능"))
# print(cabinet[5]) #error
print("hi")
print(cabinet.get(5, "사용가능")) #none 출력

print(3 in cabinet)
print(5 in cabinet)

test = {"DDG991" : "세종대왕함", "DDG992" : "율곡이이함"}
print(test["DDG991"])
test["DDG993"] = "서애류성룡함"
print(test)

del test["DDG992"]
print(test)

print(test.keys())
print(test.values())
print(test.items())

test.clear()
print(test)