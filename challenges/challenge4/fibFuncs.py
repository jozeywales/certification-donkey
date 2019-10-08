from math import sqrt, ceil

class FibMethods():
    '''A simple class that contains a fibonacci method'''

    def __init__(self):
        '''initialize'''

    def fibFormula(self, fibNum):
        if fibNum == 0:
            return 1
        return ((1+sqrt(5))**fibNum-(1-sqrt(5))**fibNum)/(2**fibNum*sqrt(5))

    def myFib(self, fibNum):
        if fibNum <= 1:
            return fibNum
        else:
            return(self.myFib(fibNum-1) + self.myFib(fibNum-2))


myTest = FibMethods()

myTest.myFib(5)