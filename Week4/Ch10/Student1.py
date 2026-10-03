class Human:
    eye = 2
    nose = 1
    mouth = 1
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(self.name, self.age)
        
    def eat(self, food):
        print(food, "먹다")
    
    def sleep(self):
        print("자다")
        
    def talk(self):
        print("말하다")
        
print("눈 개수 :", Human.eye)
lee = Human("이수근", 27)
lee.introduce()
lee.eat("치킨")

##############################
        
class Student(Human):
    def __init__(self, name, age, studentNum) :
        super().__init__(name, age)
        self.studentNum = studentNum
    def introduce(self):
        # print(self.studentNum, "학번", self.age, "살", self.name, "입니다")
        print(self.studentNum, end=" ")
        super().introduce()
    def study(self):
        print("공부하다")

if __name__ == "__main__":
    kim = Student("유재석", 17, 20201312)
    kim.introduce()
    kim.sleep()
    kim.study()