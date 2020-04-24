class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

#예외처리에 해당하는 에러가 발생했을때에, except등장
#에러의 이름에 대응하여 에러메세지 대신 가독성있는 메시지 알려주기
except ValueError:
    print("잘못된 값 입력! 한자리 수만 달라!")

except BigNumberError as errMsg:
    print("야야야 너무 크자너")
    print(errMsg)


#어쨋든 마지막에 출력해줌
finally:
    print("계산기 끝!")