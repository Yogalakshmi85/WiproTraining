from oopConcepts.myexceptions import AgeExceptions

class AgeCalc():
    def voting_age_check(self , age):
        if age < 18:
            raise AgeExceptions('Not Eligible to Vote!')
        else:
            return True

    def pension_age_check(self, age):
        if age < 60:
            raise AgeExceptions('Not Eligible for Pension')
        else:
            return True
