class Calculator:
    def __init__(self) -> None:
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(3))


#############

class FourCal:
    pass

a = FourCal()
print(type(a))
print("###########################################")
############
class FourCal:
    def __init__(self, first, second):  #생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
class MoreFourCal(FourCal):     #자식클래스
    #pass
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
        

a = FourCal(3,5)
a.setdata(2,4)
print(a.first)
print(a.second)

print(a)
print(type(a))
print(a.add())


#상속-자식클래스
a = MoreFourCal(3,2)
print(a.add())
print(a.mul())
print(a.div())

    