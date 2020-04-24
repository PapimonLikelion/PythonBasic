from random import *

candidate = []

number=1
for i in range (0,20):
    candidate.append(number)
    number+=1

print(candidate)
shuffle(candidate)
print("치킨 당첨자 :", candidate[0])
print("치킨 당첨자 :", candidate[1:4])

users = range(1,21)
print(type(users))

users = list(users)
print(type(users))

shuffle(users)
winners = sample(users, 4)

print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
