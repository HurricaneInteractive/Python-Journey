'''
    https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
    Question:
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.

    Hints:
    Use __init__ method to construct some parameters
'''

class Methods:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter String:\n")
    
    def printString(self):
        print(self.string.upper())

method = Methods()
method.getString()
method.printString()

'''
    GitHub Project Solution:
    class InputOutString(object):
        def __init__(self):
            self.s = ""

        def getString(self):
            self.s = raw_input()

        def printString(self):
            print self.s.upper()

    strObj = InputOutString()
    strObj.getString()
    strObj.printString()

'''
