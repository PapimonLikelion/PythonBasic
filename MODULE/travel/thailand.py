class ThailandPackage:
    def detail(self):
        print("태국 패키지 투어 50만원")

#내부에서 직접실행할 경우
if __name__ == "__main__":
    print("Thailand 모듈을 >>내부에서<< 직접 실행하기")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 모듈을 <<외부에서>> 직접 실행하기")