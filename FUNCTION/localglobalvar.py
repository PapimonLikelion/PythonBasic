gun = 30

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 내 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print("[함수 내] 내 남은 총: {0}".format(gun))
    return soldiers, soldiers

m16, boatswainsmate = checkpoint_ret(100, 70)
print("필승! 현재 갑판병 {1}, 총기 {0}대 소유, 훈련준비 끝!".format(m16,boatswainsmate))