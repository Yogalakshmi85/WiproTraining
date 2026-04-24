class EmployeeDetails:
    def __init__(self, emp_no, e_name, basic_pay): #init means initialization
        self.__emp_no = emp_no
        self.__e_name = e_name
        self.__basic_pay = basic_pay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    @property
    def emp_no(self):
        return self.__emp_no
    @emp_no.setter
    def emp_no(self, emp_no):
        self.__emp_no = emp_no

    @property
    def e_name(self):
        return self.__e_name

    @e_name.setter
    def e_name(self, e_name):
        self.__e_name = e_name

    @property
    def basic_pay(self):
        return self.__basic_pay

    @basic_pay.setter
    def basic_pay(self, basic_pay):
        self.__basic_pay = basic_pay

    # def get_empno(self):
    #     return self.__emp_no
    # def set_empno(self, emp_no):
    #     self.__emp_no = emp_no

    def __calculate_allowances(self):
        allowance = (self.basic_pay * self.da / 100) + (self.basic_pay * self.hra / 100)
        return allowance

    def __calculate_deduction(self):
        deduction = (self.basic_pay * self.pf / 100)
        return deduction

    def calculate_net_salary(self):
        netSal = self.basic_pay + self.__calculate_allowances() - self.__calculate_deduction()
        return netSal

