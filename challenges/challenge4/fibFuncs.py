from math import sqrt

class FibMethods():
    '''A simple class that contains a fibonacci method'''

    def __init__(self):
        '''initialize'''



    def fibFormula(self, fibNum):
        if fibNum == 0:
            return 1
        return ((1+sqrt(5))**fibNum-(1-sqrt(5))**fibNum)/(2**fibNum*sqrt(5))
