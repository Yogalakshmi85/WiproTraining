Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dict1={1: 10, 2: 20, 3: 30}
dict1
{1: 10, 2: 20, 3: 30}
dict1[1]
10
>>> dict2={'a':10, 'b': 20, 'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['c']
30
>>> stu = {'rno': 178, 'sname': 'Cooper', 'City': 'UK'}
>>> stu
{'rno': 178, 'sname': 'Cooper', 'City': 'UK'}
>>> stu['rno']
178
>>> stu['sname']='Ross'
>>> stu
{'rno': 178, 'sname': 'Ross', 'City': 'UK'}
>>> stu['fname']='Karev'
>>> stu
{'rno': 178, 'sname': 'Ross', 'City': 'UK', 'fname': 'Karev'}
>>> stu['hosteller']=False
>>> stu
{'rno': 178, 'sname': 'Ross', 'City': 'UK', 'fname': 'Karev', 'hosteller': False}
>>> stu.get('fname')
'Karev'
>>> stu.keys()
dict_keys(['rno', 'sname', 'City', 'fname', 'hosteller'])
>>> stu.values()
dict_values([178, 'Ross', 'UK', 'Karev', False])
>>> stu.pop('hosteller')
False
>>> stu
{'rno': 178, 'sname': 'Ross', 'City': 'UK', 'fname': 'Karev'}
