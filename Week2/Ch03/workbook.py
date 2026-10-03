# if True :
#       if False:
#           print("1")
#           print("2")
#       else:
#           print("3")
# else :
#       print("4")
# print("5")

# if int(input("숫자 입력: ")) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# num = int(input("숫자 입력: "))

# if num + 20 > 255:
#     print(255)
# else:
#     print(num + 20)


# num = int(input("숫자 입력: "))

# if num - 20 < 0:
#     print(0)
# elif num + 20 > 255:
#     print(255)
# else:
#     print(num - 20)

score = int(input("score: "))

if score < 0 or score > 100:
    print("잘못된 점수입니다.")
elif score >= 81:
    print("grade is A")
elif score >= 61:
    print("grade is B")
elif score >= 41:
    print("grade is C")
elif score >= 21:
    print("grade is D")
else:
    print("grade is E")