class Cexm:
    def fsam(self):
        print("멤버 함수 메서드")
    def fsbm(self, pa):
        self.x = pa
        print("멤버변수는 x", self.x)
ca = Cexm()
ca.fsam()
ca.fsbm(5)