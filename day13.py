class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,value):
        self.value += value
        return self.value

    def min(self,value):
        self.value -= value
        return self.value

    def div(self,value):
        try:
            self.value /= value
        except ZeroDivisionError:
            print('0으로 나누지마라....')
        return self.value

    def mul(self,value):
        self.value *= value
        return self.value

a = Calculator()
print(a.add(4))
print(a.min(1))
print(a.div(0))
print(a.div(2))
print(a.mul(3))