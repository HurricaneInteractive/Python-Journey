'''
    https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
    Question:
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
    Suppose the following input is supplied to the program:
    8
    Then, the output should be:
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

    Hints:
    In case of input data being supplied to the question, it should be assumed to be a console input.
    Consider use dict()
'''

def integral_dictory(i):
    dic = {}
    for x in range(1, i+1):
        dic[x] = x * x
    return dic

i = int(input("Enter interger:\n"))
print(integral_dictory(i))

'''
    GitHub Project Solution:
    n=int(raw_input())
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i

    print d
'''