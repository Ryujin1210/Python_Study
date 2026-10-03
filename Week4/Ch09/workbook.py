class Phone: 
    def __init__(self, company, year, color):
        print("휴대폰 생성")
        self.company = company
        self.year = year
        self.color = color  
    
    def info(self):
        print(self.company, self.year, self.color)
    
    def setInfo(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color
        
my_phone = Phone("Apple", "2022", "purple")
my_phone.info()