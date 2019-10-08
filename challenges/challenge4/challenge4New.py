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
        idx = i
        lessThan20 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                      9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                      16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
        tensDigits = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
                      9: "ninety"}
        decimalGroups = {0: "", 1: "hundred", 2: "thousand", 3: "million", 4: "billion", 5: "trillion"}
        numText = ''
        numTwoDigits = ''
        self.digitText = ''
        numLength = len(str(result))
        self.numText = str(result)
        numberInfo = NumberInfo()
        numGroups = numberInfo.getNumOfGroups(result)

        '''Determine what digits are in the most significant group (msg) of 3 digits'''
        while i <= numGroups:
            if divmod(numLength,3)[1] == 1: # determine if msg has 1 digit
                self.digitText = lessThan20.get(int(self.numText[idx])) + ' ' + decimalGroups.get(numGroups) + ' '# get the english text
                numLength -= 1
                idx += 1
            elif divmod(numLength,3)[1] == 2: # determine if msg has 2 digits
                numTwoDigits += self.numText[i] + self.numText[i+1] # concatenate the msg of 2 digits
                if int(numTwoDigits) < 20:
                    self.digitText += lessThan20.get(int(numTwoDigits)) + ' ' + decimalGroups.get(numGroups) + ' ' # 10, 11, 12, 13.. + hundred, thousand, ...
                else:
                    self.digitText += tensDigits.get(int(numTwoDigits[0])) + ' ' + lessThan20.get(int(numTwoDigits[1]))  + ' ' \
                                      + decimalGroups.get(numGroups) + ' '    # + hundred, thousand, million...
                numLength -= 2
                idx += 2
            elif divmod(numLength,3)[1] == 0:    # msg has 3 digits
                #print(lessThan20.get(self.numText[idx]))
                if lessThan20.get(self.numText[idx]) != None:
                    self.digitText += lessThan20.get(int(self.numText[idx])) + ' ' + decimalGroups.get(1) + ' '
                if int((self.numText[idx+1])+(self.numText[idx+2])) < 20:  # if 2 digit number in the tens or ones place is < 20
                    if numGroups > 1:
                        self.digitText += lessThan20.get(int((self.numText[idx+1]) + self.numText[idx+2])) + ' ' + decimalGroups.get(numGroups) + ' '
                    else:
                        self.digitText += lessThan20.get(int((self.numText[idx + 1]) + self.numText[idx + 2]))
                elif numGroups > 1:
                    if (int(self.numText[idx+2])) == 0:
                        self.digitText += (tensDigits.get(int(self.numText[idx+1])) + lessThan20.get(int(self.numText[idx+2])) + ' ' + decimalGroups.get(numGroups) + ' ')
                    else:
                        self.digitText += (tensDigits.get(int(self.numText[idx+1])) + ' ' + lessThan20.get(int(self.numText[idx+2])) + ' ' + decimalGroups.get(numGroups) + ' ')
                else:
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