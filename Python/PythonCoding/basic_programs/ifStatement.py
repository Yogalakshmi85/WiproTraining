#greatest of 2 numbers

"""
Date: 22-04-26
Desc: Working on If statements
"""
from random import choice

'''
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a another number:"))

if num1 > num2 :
    print("The greatest number is " ,num1)
elif num1 == num2:
    print("Both are equal")
else :
    print("The greatest number is ", num2)
'''

#biggest among 3

'''num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    print("The greatest number is ", num1)
elif num2 > num1 and num2 > num3:
    print("The greatest number is ", num2)
elif num3 > num1 and num3 > num2:
    print("The greatest number is ", num3)
elif num1 == num2 and num2 == num3:
    print("All numbers are equal")
else:
    print("Two numbers are equal")'''

#week day

ch = int(input("Enter your choice between 1 to 7:"))

match ch:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid case")
