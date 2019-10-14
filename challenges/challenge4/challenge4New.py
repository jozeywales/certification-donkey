import unittest
from cmath import e
from math import ceil
from challenges.challenge4.fibFuncs import FibMethods
from challenges.challenge4.MiscMethods import NumberInfo


class Challenge4(unittest.TestCase, FibMethods):

    def test_begin(self):
        #self.driver = webdriver.Chrome("../chromedriver.exe")
        #answer = fibFuncs.fibLooping(5)
        #answer = fibFuncs.fibRecursive(2)
        my_fibMethods = FibMethods()
        answer = ceil(my_fibMethods.fibFormula(38))
        self.convertToText(answer)
        self.displayResult()


    def convertToText(self, result):
        i = 0
        idx = i # group of 3 index
        lessThan20 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                      9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                      16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
        tensDigits = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
                      9: "ninety"}
        decimalGroups = {0: "", 1: "hundred", 2: "thousand", 3: "million", 4: "billion", 5: "trillion"}

        numTwoDigits = ''
        self.digitText = ''
        numLength = len(str(result))
        self.numText = str(result)
        numberInfo = NumberInfo()
        numGroups = numberInfo.getNumOfGroups(result)   # get the length of number in 3 digit groups

        '''Begin by determining what digits are in the most significant group (msg) of 3 digits of the number, R to L'''
        while i <= numGroups:
            if divmod(numLength,3)[1] == 1: # determine if msg is 1 digit in length
                self.digitText = lessThan20.get(int(self.numText[idx])) + ' ' + decimalGroups.get(numGroups) + ' '# get the english text
                numLength -= 1
                idx += 1
            elif divmod(numLength,3)[1] == 2: # determine if msg is 2 digits in length
                numTwoDigits += self.numText[i] + self.numText[i+1] # concatenate the msg of 2 digits
                if int(numTwoDigits) < 20:
                    self.digitText += lessThan20.get(int(numTwoDigits)) + ' ' + decimalGroups.get(numGroups) + ' ' # 10, 11, 12, 13.. + hundred, thousand, ...
                else:
                    self.digitText += tensDigits.get(int(numTwoDigits[0])) + ' ' + lessThan20.get(int(numTwoDigits[1]))  + ' ' \
                                      + decimalGroups.get(numGroups) + ' '    # + hundred, thousand, million...
                numLength -= 2
                idx += 2
            elif divmod(numLength,3)[1] == 0:    # is msg 3 digits in length
                #print(lessThan20.get(self.numText[idx]))
                if lessThan20.get(self.numText[idx]) != None: # check for a digit is in the hundreds place
                    self.digitText += lessThan20.get(int(self.numText[idx])) + ' ' + decimalGroups.get(1) + ' ' # get how many hundred
                if int((self.numText[idx+1])+(self.numText[idx+2])) < 20:  # the right most 2 digit number of 3 digits is < 20
                    if numGroups > 1: # number is > 999
                        self.digitText += lessThan20.get(int((self.numText[idx+1]) + self.numText[idx+2])) + ' ' + decimalGroups.get(numGroups) + ' '
                    else: # number is < 1000
                        self.digitText += lessThan20.get(int((self.numText[idx + 1]) + self.numText[idx + 2])) # if the right most 2 digit number of 3 digits > 19
                elif numGroups > 1: # number > 999
                    if (int(self.numText[idx+2])) == 0: # the 3 digit group is zero based but the right most 2 of 3 numbers > 19
                        self.digitText += (tensDigits.get(int(self.numText[idx+1])) + lessThan20.get(int(self.numText[idx+2])) + ' ' + decimalGroups.get(numGroups) + ' ')
                    else: # > 19 but not zero based
                        self.digitText += (tensDigits.get(int(self.numText[idx+1])) + ' ' + lessThan20.get(int(self.numText[idx+2])) + ' ' + decimalGroups.get(numGroups) + ' ')
                else: # < 1000 and right most 2 digits > 20
                    self.digitText += (tensDigits.get(int(self.numText[idx + 1])) + ' ' + lessThan20.get(int(self.numText[idx + 2])))
                numLength -= 3
                idx += 3
            numGroups -= 1
            if numGroups != 1:  # no need to increment i on the last group of 3 digits
                i += 1



    def displayResult(self):
        print(self.numText + ' - ' + self.digitText)




if __name__ == '__main__':
    unittest.main()