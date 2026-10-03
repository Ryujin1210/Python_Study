class Cadd:
    def fadd(self, a, b):
        self.x = a
        self.y = b
        self.hap = self.x + self.y

obj = Cadd()
obj.fadd(10, 20)
print(obj.x, obj.y, obj.hap)        