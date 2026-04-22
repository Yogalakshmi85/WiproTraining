#natural numbers

'''num = int(input("Enter the range:"))

sum=0

for i in range (1, num+1):
    sum = sum + i ** 2

print('Sum of squares of natural numbers: ', sum)'''

#print asterisks

num = int(input("How many * you want:"))

for _ in range(1, num+1):
    print('*', '&', sep='^', end='\t')