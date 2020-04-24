subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유","돈","노"]
print(subway.index("유"))

subway.append("하")
print(subway)

subway.insert(1,"정")
print(subway)

subway.pop()
print(subway)

subway.pop()
print(subway)

subway.pop()
print(subway)

subway.append("유")
print(subway)
print(subway.count("유"))

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

mix_liszt = ["조세호", 10, True]
print(mix_liszt)

num_list.extend(mix_liszt)
print(num_list)