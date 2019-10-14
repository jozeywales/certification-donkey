class NumberInfo():
    '''A simple class to get the number of 3 digit groups in an integer'''

    def __init__(self):
        '''initialize'''

    def getNumOfGroups(self, num):
        '''determine total number groups in an integer, ie. 23456 has 2 groups'''
        numStr = str(num)
        if divmod(len(numStr),3)[1] == 0:
            return divmod(len(numStr),3)[0] # get number of groups of exactly 3 digits
        else:
            return divmod(len(numStr),3)[0]+1   # same as above plus the group with less than 3 digits