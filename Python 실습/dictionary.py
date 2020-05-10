#딕셔너리(내장함수)
pairs = {'하현우' : '우리동네 음악대장',
         '정동하' : '에헤라디오',
         '고영배' : '궤종시계' }

#하나의 키-발류 추가하는 방법
#딕셔너리형 변수[키]=발류
print(pairs)
pairs['유회승'] = '게임보이'
print(pairs)

#키발류 삭제 
#del 변수[키]

del pairs['정동하']
print(pairs)

#Key로 Value 얻기 : 변수.get(KEY)
qs = pairs.get('하현우')
print(qs)