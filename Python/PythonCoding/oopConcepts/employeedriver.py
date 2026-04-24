from oopConcepts.employeedetails import EmployeeDetails

#driver

eno = int(input('Enter employee number: '))
ename = input('Enter employee name: ')
bp = float(input('Enter basic pay: '))

employee = EmployeeDetails(emp_no = eno, e_name = ename, basic_pay = bp) #creates objects and automatically calls constructor(init)
#where employee is the OBJECT REFERENCE VARIABLE NOT OBJECT


print('Employee no: ', employee.emp_no)
print('Employee name: ', employee.e_name)
print('Employee Basic salary: ', employee.basic_pay)
print('Employee Salary: ', employee.calculate_net_salary())


