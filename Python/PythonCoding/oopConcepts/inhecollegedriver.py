#driver

from oopConcepts.college import College
from oopConcepts.student import Student
from oopConcepts.studentgrade import StudentGrade
from oopConcepts.teacher import Teacher

cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('City: ')

srno = int(input('S Roll no: '))
sn = input('S Name: ')
m1 = int(input('Mark 1: '))
m2 = int(input('Mark 2: '))
m3 = int(input('Mark 3: '))

eid = int(input('E id: '))
en = input('Teacher Name: ')
de = input('Dept Name: ')
bp = float(input('Enter Basic Pay: '))

# project = College(ccode = cc, cname = cn, ccity = ci)
#
# project.welcome_message()
# project.display_college_details()

# project = Student(ccode=cc, cname=cn, ccity=ci, rno=srno, sname=sn, m1=m1, m2= m2, m3=m3)

project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno=srno, sname=sn, m1=m1, m2=m2, m3=m3)
project.welcome_message()
project.display_college_details()

print(f'Roll no: {project.rollno} \nName: {project.stuname} \n'
      f'Total: {project.calculate_total()} \nAverage: {project.calculate_avg()}')

project.calculate_grade()

print(f'Result : {project.result} \nGrade : {project.grade}')

teacher = Teacher(ccode=cc, cname=cn, ccity=cc, eid=eid, tn=en, de=de, bp=bp)
print(f'Emp id: {teacher.empid} \nTeacher Name: {teacher.tname} \n'
      f'Department: {teacher.dept} ')
print(f'Salary: {teacher.calculate_salary()}')
