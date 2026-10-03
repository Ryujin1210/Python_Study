# class Bag:
#     def __init__(self):
#         self.data = []
    
#     def add(self, x):
#         self.data.append(x)
        
#     def addtwice(self, x):
#         self.add(x)
#         self.add(x)
        
class Bag:
    call_name = '가방'
    def __init__(self, x):
        self.data = []
        self.call_name = x
        
    def add(self, x):
        print("넣는다")
        self.data.append(x)
        
    def open(self):
        print("열다")
                
    def close(self):
        print("닫다")
        
    def remove(self, x):
        print("꺼내다")
        self.data.remove(x)
        
    def addtwice(self, x):
        self.add(x)
        self.add(x)
    
eco_bag = Bag("에코백")
print(eco_bag.call_name)
eco_bag.add("생수")
eco_bag.add("과자")
eco_bag.remove("생수")

   
handbag = Bag("핸드백")
print(handbag.call_name)
handbag.add("이어폰")
handbag.add("휴대품")
handbag.remove("이어폰")
print(handbag.data)

sports_bag = Bag("스포츠백")
print(sports_bag.call_name)
sports_bag.add("바나나")
sports_bag.add("프로틴")
sports_bag.remove("바나나")
sports_bag.addtwice("영양제")
print(sports_bag.data)