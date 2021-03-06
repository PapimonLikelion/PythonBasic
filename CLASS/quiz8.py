# Quiz)주어진 코드를 활용하여 부동산 프로그램을 작성하시오
# (출력 예제)
# 총 3대의 매물이 있다.
# - 강남 아파트 매매 10억 2010년
# - 마포 오피스텔 전세 5억 2007년
# - 송파 빌라 월세 500/50 2000년

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{0} {1} {2} {3}억 {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

class monthly(House):
    def __init__(self, location, house_type, deal_type, price, completion_year, monthly_pay):
        super().__init__(location, house_type, deal_type, price, completion_year)
        self.monthly_pay = monthly_pay
    
    def show_detail(self):
        print("{0} {1} {2} {3}/{5} {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year, self.monthly_pay))

houses = []
house1 = House("강남", "아파트", "매매", 10, 2010)
house2 = House("마포", "오피스텔", "전세", 5, 2007)
house3 = monthly("송파", "빌라", "월세", 500, 2000, 50)

houses.append(house1)
houses.append(house2)
houses.append(house3)

for house in houses:
    house.show_detail()