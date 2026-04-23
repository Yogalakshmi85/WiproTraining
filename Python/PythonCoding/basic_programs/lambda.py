# num1 = int(input('Enter n1: '))
# num2 = int(input('Enter n2: '))
#
# add = lambda n1, n2: n1 + n2
#
# print(add(num1, num2))


numbers = [1, 5, 2, 3, 4]
#
# sq = lambda  nums: [n * n for n in nums] # if {} then the answer is sorted in tree based
#
# print(sq(numbers))

sq = lambda  nums: [n * n for n in nums if n % 2 == 0]

print(tuple(sq(numbers)))