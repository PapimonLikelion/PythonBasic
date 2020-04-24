site = "http://naver.com"
withouthttp = site[7:]
print(withouthttp)
withoutcom = withouthttp[:-4]
print(withoutcom)
password = withoutcom[:3] + str(len(withoutcom)) + str(withoutcom.count('e')) + "!"
print(password)

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0}의 비밀번호는 {1}입니다. ".format(url, password))