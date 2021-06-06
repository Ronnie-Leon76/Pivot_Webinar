class Numbers():
    def __init__(self,val):
        val = 1
        self.val = val
   

class NaturalNumbers(Numbers):
    def __init__(self, val):
        super(NaturalNumbers,self).__init__(val)
    def setNaturalNumber(self,val1):
        if(int(val1>0)):
            self.val = val1
    def getNaturalNumber(self):
        return self.val

class Integers(Numbers):
    def __init__(self, val):
        super(Integers,self).__init__(val)
    def setInteger(self,int_number):
        if(int_number >= 0 or int_number <= 0):
            self.val = int_number
    def getInteger(self):
            return self.val

class RealNumber(Numbers):
    def __init__(self, val):
        super(RealNumber,self).__init__(val)
    def setRealNumber(self,real_number):
        if(real_number >= 0.0 or real_number <= 0.0):
            self.val = real_number
    def getRealNumber(self):
            return self.val


num = int(input("Enter the number: "))
obj = NaturalNumbers(num)
obj.setNaturalNumber(num)
print(obj.getNaturalNumber())
    
    



"""
num = int(input("Enter a number : "))
if num > 1:
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
        else:
            print(num,"is a prime number")
else:
    print(num,"is not a prime number")
"""

    
