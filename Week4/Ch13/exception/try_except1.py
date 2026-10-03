# while True:
#     try:
#         x = int(input("숫자만 입력하시오"))
#         break
#     except ValueError:
#         print("숫자가 아닙니다!")
#     finally:
#         pass

while True:
    try:
        print("명령어1")
        x = int(input("숫자만 입력하시오")) # ValueError
        #'2' + x                         # TypeError
        print("명령어2")
        break
    except TypeError:
        print("데이터 타입이 다릅니다")
    except ValueError as e: 
        print("입렵값이 숫자가 아닙니다!")
        print("에러 관련 정보", e)
    except (ZeroDivisionError,  NameError):
            print("한번에 여러개")
    finally:
        print("finally 동작")
print("프로그램 완료")