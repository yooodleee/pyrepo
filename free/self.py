####################
## self
####################


# %%
# %%
class Calculator:
    result = 0 

    def add(self, n):
        self.result += n # result: member variable -> class instance 

    def sub(self, n):
        self.result -= n


cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

cal1.add(4)
cal2.add(19)
cal3.sub(5)

cal3.sub(56)
cal3.sub(27)


print(f"1st calculated result: {cal1.result}")
# output: 1st calculated result: 4

print(f"2nd calculated result: {cal2.result}")
# output: 2nd calculated result: 19

print(f"3rd calculated result: {cal3.result}")
# output: 3rd calculated result: -88


type(print(cal1))
# output: <__main__.Calculator object at 0x000001121B93AB50>

type(print(cal2))
# output: <__main__.Calculator object at 0x000001121B93AB20>

type(print(cal3))
# output: <__main__.Calculator object at 0x000001121CBFA460>


# %%
class Calculator2:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    
    def sum(self):
        result = self.m + self.n
        return result

    def sub(self):
        result = self.m - self.n 
        return result
    
    def mul(self):
        result = self.m * self.n 
        return result
    
    def div(self):
        result = self.m / self.n 
        return result


cal1 = Calculator2(13, 3)
cal2 = Calculator2(11, 7)
cal3 = Calculator2(18, 8)
cal4 = Calculator2(9, 5)

cal1.sum()
cal2.sub()
cal3.mul()
cal4.div()


# %%
