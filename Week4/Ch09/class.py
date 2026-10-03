class Pizzaclass:
    def order(self):
        print("주문하다. ")
        self.kind=10
    large = 21
## 객체 생성 
# 객체 변수명 = 클래스명() # 생성자 함수 
pizza1 = Pizzaclass()
pizza1.order()
print(pizza1.large)
print(pizza1.kind)