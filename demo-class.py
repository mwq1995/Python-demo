class Calculator:
    def __init__(self,name,price,height,width,weight):
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight

    def add(self,x,y):
        result = x+y
        print(result)
    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

cal = Calculator('111',1,1,1,1)
print(cal.name)
print(cal.price)
cal.add(10,11)
cal.divide(13,2)
