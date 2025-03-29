from OopDemo import Calculator


class ChildImplementation(Calculator):
    num1 = 100

    def getCompleteData(self):
        return self.num1 + self.num + self.summation()

    def __init__(self):
        Calculator.__init__(self, 2, 10)


obj2 = ChildImplementation()
print(obj2.getCompleteData())


