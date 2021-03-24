from exce import ValueToLarge, ValueToSmall, ZeroNotDivisible

class Cal_Cu():

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b
    
    def mod(self):
        return self.a%self.b

