#바로 임포트는 모듈만
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.vietnam import VietnamPackage
trip_to = VietnamPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
