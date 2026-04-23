# #function
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def diff(n1, n2):
#     return n1 - n2
#
#
# def product(n1, n2):
#     return n1 * n2
#
# #driver
#
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))
#
# print('Sum is ', add(num1, num2))
# print('Difference is ', diff(num1, num2))
# print('Product is ', product(num1, num2))


#list iteration using functions
#
# def add(nums):
#     sum = 0
#     for n in nums:
#         sum += n
#
#     return  sum
#
# numbers = list()
#
# count = int(input('How many numbers you want :'))
#
# for _ in range(1, count+1):
#     numbers.append(int(input('Number: ')))
#
# print('Sum is ', add(numbers))


#Arbitary
#
# def add(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#
#     return  sum
#
# print(add(2,3,4))
# print(add(4,5,7,9))


#optional

def add(n1, n2, n3=10):
    return n1 + n2 + n3

num1 = int(input('Enter n1: '))
num2 = int(input('Enter n2: '))

print(add(num1, num2, 70))