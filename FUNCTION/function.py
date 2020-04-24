def open_account():
    print("새로운 계좌 개설")

open_account()

def deposit(balance, money):
    print("입금이 완료됨, 잔액은 {0}".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료됨, 잔액은 {0}".format(balance-money))
        return balance-money
    else:
        print("출금 힘들어 돈없어, 잔액은 {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    #튜플 형식으로 반환
    return commission, balance-money-commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 300)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이고, 잔액 {1}이다.".format(commission, balance))

def lecture(name, age=22, major="CSE"):
    print("이름은 {0}, 나이는 {1}, 전공은 {2}".format(name,age,major))

lecture("조영상",24)
lecture("장찬",24)
lecture("박수형",24,"MNE")
lecture("이재현",major="경영")

#가변인자를 매개변수로
def profile(name, age, *language):
    print("이름: {0} 나이 :{1}".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("조영상", 24, "C++", "C", "Python", "html/css") 
profile("박지훈", 25)