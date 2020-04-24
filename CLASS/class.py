#일반유닛
class Unit:
    #constructor
    def __init__(self, name, hp, damage, speed =0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def move(self, location):
        print("[지상 돌격]")
        print("{0}은 {2}로 SPEED{1}로 돌진!".format(self.name, self.speed, location))

#instance
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 :{1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
#adding member var
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다. ".format(wraith2.name))


#공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 대미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃" , 50, 100)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

#Heal medic
class Medic(Unit):
    def __init__(self, name, hp, damage, heal):
        super().__init__(name, hp, damage)
        self.heal = heal

    def healing(self):
        print("저의 이름은 {1}, 의사죠. 당신을 {0}만큼 치료합니다.".format(self.heal, self.name))


medic = Medic("메딕", 10, 10, 100)
medic.healing()

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, location):
        print("{0} 방향으로 저 {1}는 날라갑니다. ".format(location, self.name))
    
class FlyingUnit(Flyable, Unit):
    def __init__(self, name, hp, damage, flying_speed):
        Unit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 돌격]")
        self.fly(location)
    
vulture = Unit("벌쳐", 100, 30, 50)
vulture.move("12시")

battlecru = FlyingUnit('배틀크루저', 1000, 1000, 1000)
battlecru.move("3시")