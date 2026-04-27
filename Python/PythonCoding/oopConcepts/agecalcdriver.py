from oopConcepts.agecalc import AgeCalc
from oopConcepts.myexceptions import AgeExceptions

age = int(input('Enter age:'))

aobj = AgeCalc()

try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
except AgeExceptions as ae:
    print(ae)
else:
    print('Eligible to vote.')
finally:
    print('Done.')
