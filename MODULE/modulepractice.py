import theater_module
theater_module.price(3) #3명이서 영화보러갔을때 가격
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv
mv.price_soldier(4)
mv.price(3)

from theater_module import *
price(3)
price_soldier(7)
price_morning(4)

from theater_module import price, price_morning
price(10)
price_morning(100)