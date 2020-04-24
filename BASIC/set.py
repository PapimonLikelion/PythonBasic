#집합 set
#중복 x, 순서 x
my_set = {1,2,3,3,3}
print(my_set)

java = {"유", "조", "돈"}
python = set(["유", "조", "김"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java - python)
print(java.difference(python))

#python 인력 추가
python.add("김2")
print(python)

#python 뺴기
python.remove("김")
print(python)