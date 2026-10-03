# class Human:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#     def intro(self):
#         print(str(self.age) + "살" + self.name + "입니다.")

# kim = Human(29, "김상형")
# kim.intro()
# lee = Human(45, "이승우")
# lee.intro()


def to_temp(text: str) -> float:
    return float(text)

print(to_temp("82.5"))
print(to_temp("N/A"))
print("프로그램 끝")
