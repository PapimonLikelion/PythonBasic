#animal package
#dog, cat modules
#dog, cat modules can say "hi"

# from animal import dog  #animal패키지 에서 dog모둘 부탁해
# from animal import cat

# from animal import * #다 갖고와

# d = dog.Dog()
# d.hi()
# c = cat.Cat()
# c.hi()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("범서읍 점촌2길 32")
print(location)
print(location.longitude)
print(location.latitude)
print(location.raw)
