#방법 1
print("나는 %d살 입니다. " %20)
print("나는 %s살 입니다. " %20)
print("나는 %s를 좋아해요. " %"파이썬")
print("Apple은 %c로 시작해요. " %'A')
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

#방법 2
print("나는 {}살 입니다. ".format(20))
print("나는 {}색과 {}색을 좋아해요. ".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요. ".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요. ".format("파란","빨간"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요. ".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요. ".format(color="빨간", age=20))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, \n {color}색을 좋아해요.")

#endline 탈출문자
print('저는 "조영상"입니다')
print("저는 \"조영상\"입니다")
print("배워야할게 \n 많다")

#\r
print("red Apple\rPine")

#\b
print("Redd\bApple")

#\를 문장에서 쓰려면\\로 쓰기
print("\\과연")