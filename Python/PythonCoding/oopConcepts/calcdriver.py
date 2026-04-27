from oopConcepts.calc import Calc

cobj = Calc()

print(cobj.add(10, 5))
print(cobj.sub(10, 5))
print(cobj.mul(10, 5))

numbers = [10, 20, 30]
count = len(numbers)
print(f'Length: {count}')
try:
    res = cobj.fdiv(10, 0)
    for i in range(0, count+1):
        print(numbers[i])
except IndexError:
    print('Check the index')
except ZeroDivisionError:
    print("A number can't be divided by 0")
except:
    print('Oops!! Something went wrong!!')
else:
    print(res)
finally:
    print('Done..')


