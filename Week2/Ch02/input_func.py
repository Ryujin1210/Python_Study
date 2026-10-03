sa = input("문자열을 입력하세요.\n")
#print(input("문자열을 입력하세요.\n"))
print(sa)

print(type(sa))

print("=================================")

ia = input("정수를 입력하세요.\n")

print(ia)
print(type(int(ia)))

print("=================================")

print("첫 번째 정수를 입력하세요.")
ra = input()
rb = input("두 번째 정수를 입력하세요.\n")
rc =ra + rb
print("두 수의 합은", rc, "입니다.")

print("=================================")

#print("두 수의 합은", int(input("첫 번째 정수를 입력하세요.\n")) + int(input("두 번째 정수를 입력하세요.\n")), "입니다.")
print(f"두 수의 합은 {int(input('첫 번째 정수를 입력하세요.\n')) + int(input('두 번째 정수를 입력하세요.\n'))}입니다.")

print("=================================")

a = int(input("첫 번째 정수를 입력하세요.\n"))
b = int(input("두 번째 정수를 입력하세요.\n"))
print(f"두 수의 합은 {a + b}입니다.")