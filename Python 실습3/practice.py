class Person:
    #initialize name인자 받아서 변수에 넣어라
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #self... 만들어진 물체의 변수를 활용해야 할때
    def say_hello(self,to_name):
        print(to_name + "야 " + self.name + " 안녕!")
    
    def introduce(self):
        print("내 이름은 "+self.name + "그리고 나는 "+ str(self.age))

#class 새로운거(상속할것)
class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포댓다 "+ to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음에 뭐 만들지 "+to_program)

joel = Person("영상", 20)
jaehyun = Police("재현", 20)
mike = Programmer("마이크",22)

joel.introduce()
jaehyun.introduce()
mike.introduce()
jaehyun.arrest("영상")
mike.program("클라")