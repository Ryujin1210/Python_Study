class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 먹는다.")

    def sleep(self):
        print(f"{self.name}가 잔다.")

    def sound(self):
        print("동물이 소리를 낸다.")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}살")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def sound(self):
        print("야옹")
        super().sound()

    def scratch(self):
        print(f"{self.name}가 발톱으로 긁는다.")

    def info(self):
        super().info()
        print(f"털 색깔: {self.color}")



cat1 = Cat("나비", 3, "회색")

cat1.info()
cat1.eat()
cat1.sleep()
cat1.sound()
cat1.scratch()

