import unittest
from cmath import e
from math import ceil
from challenges.challenge4.fibFuncs import FibMethods


class Challenge4(unittest.TestCase):

    def test_begin(self):
        #self.driver = webdriver.Chrome("../chromedriver.exe")
        #answer = fibFuncs.fibLooping(5)
        #answer = fibFuncs.fibRecursive(2)
        myFibAnswer = FibMethods()
        answer = ceil(myFibAnswer.myFib(20))
        self.numToText(answer)

    # fibonacci number to english translation
    def numToText(self, result):
        i=0
        digitTxt = ''
        numText = str(result)
        lessThan20 = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",
                     10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
                     17:"seventeen",18:"eighteen",19:"nineteen"}
        tensDigits = {1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
        decTerms = {0:"hundred",1:"thousand",2:"ten thousand",3:"hundred thousand",4:"million",5:"billion",6:"trillion",7:"quadrillion",8:"quintillion"}

        #print(len(numText))
        if len(numText) < 3:
            if int(numText) < 20:
                digitTxt = lessThan20.get(int(numText))
            elif int(numText) > 19 and int(numText) < 100:
                while i < len(numText):
                    digitTxt = tensDigits.get(int(numText[int(i)])) + '-'
                    i += 1
                    digitTxt += lessThan20.get(int(numText[int(i)]))
                    break
            print(numText + ' - ' + digitTxt)
        elif len(numText) == 3:     # for numbers in the hundreds
            while i < len(numText):
                digitTxt += lessThan20.get(int(numText[int(i)])) + ' ' + decTerms.get(i) + ' '
                i += 1
                if numText[1] != '0':
                    digitTxt += tensDigits.get(int(numText[i])) + ' '
                else:
                    digitTxt += ''
                i += 1
                if numText[2] != '0':
                    digitTxt += lessThan20.get(int(numText[int(i)]))
                else:
                    digitTxt += ''
                i += 1
            print(numText + ' - ' + digitTxt)
        elif len(numText) == 4:     # for numbers in the thousands
            while i < len(numText):
                digitTxt += lessThan20.get(int(numText[int(i)])) + ' ' + decTerms.get(i+1) + ' '
                i += 1
                if numText[0] != '0':
                    digitTxt += lessThan20.get(int(numText[int(i)])) + ' '
                else:
                    digitTxt += ''
                if numText[1] != '0':
                    digitTxt += decTerms.get(i-1) + ' '
                else:
                    digitTxt += ''
                i += 1
                if numText[2] != '0':
                    digitTxt += tensDigits.get(int(numText[i])) + ' '
                else:
                    digitTxt += ''
                i += 1
                if numText[3] != '0':
                    digitTxt += lessThan20.get(int(numText[int(i)])) + ' '
                else:
                    digitTxt += ''
                i += 1
            print(numText + ' - ' + digitTxt)



if __name__ == '__main__':
    unittest.main()
