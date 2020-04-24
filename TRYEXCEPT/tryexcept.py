try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

#예외처리에 해당하는 에러가 발생했을때에, except등장
#에러의 이름에 대응하여 에러메세지 대신 가독성있는 메시지 알려주기
except ValueError:
    print("잘못된 값 입력!")

except ZeroDivisionError as err:
    print(err)


try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

#예외처리에 해당하는 에러가 발생했을때에, except등장
#에러의 이름에 대응하여 에러메세지 대신 가독성있는 메시지 알려주기
except Exception as err:
    print(err)

except:
    print("알 수 없는 에러가 발생했어요")
