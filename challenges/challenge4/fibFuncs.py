from math import sqrt

class FibMethods():
    '''A simple class that contains a fibonacci method'''

    def __init__(self):
        '''initialize'''

    def fibLooping(self, fibNum):
        a,b = 1,1
        for i in range(fibNum-1):
            a,b = b,a+b
        return a

    def fibRecursive(self, fibNum):
        if fibNum == 1 or fibNum == 2:
            return 1
        return self.fibRecursive(fibNum-1) + self.fibRecursive(fibNum-2)

    def myFib(self, fibNum):
        if fibNum == 0:
            return 1
        return ((1+sqrt(5))**fibNum-(1-sqrt(5))**fibNum)/(2**fibNum*sqrt(5))
