class Calculator:
    num = 100 # class variables

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b


    def getData(self):
        print("Simple Calculator")

    def summation(self):
        return self.firstNum + self.secondNum + self.num

obj = Calculator(2, 3)
print(obj.getData()) #out put NONE
obj.getData()
print(obj.summation())

obj1 = Calculator(3, 4)
print(obj1.getData()) #out put NONE
obj1.getData()
print(obj1.summation())