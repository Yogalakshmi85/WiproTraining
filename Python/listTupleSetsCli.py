Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
id(s1)
1814380950944
s2='hi'
id(s2)
140707956602296
s3=s1
id(s3)
1814380950944
list1 =[10,2,3,4}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
list1 =[10,2,3,4]
list1
[10, 2, 3, 4]
type(list1)
<class 'list'>
list1[0]
10
list1[3]
4
list1[-1]
4
list1[0:2]
[10, 2]
list1[0,3,2]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list1[0,3,2]
TypeError: list indices must be integers or slices, not tuple
list1[0:3:2]
[10, 3]
s1
'hello'
list2=list(s1)
list2
['h', 'e', 'l', 'l', 'o']
list3 = list1
list3
[10, 2, 3, 4]
id(list1)
1814410151232
id(list3)
1814410151232
list4=[100, 'hii', 67.90, 'tom', True]
list4
[100, 'hii', 67.9, 'tom', True]
list4[2]='jerrry'
list4
[100, 'hii', 'jerrry', 'tom', True]
list4[5]=67.90
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list4[5]=67.90
IndexError: list assignment index out of range
list4.append(67.90)
list4
[100, 'hii', 'jerrry', 'tom', True, 67.9]
list4.remove('tom')
list4
[100, 'hii', 'jerrry', True, 67.9]
list4.count(100)
1
list4.insert(2, 'hii')
list4
[100, 'hii', 'hii', 'jerrry', True, 67.9]
list4.pop()
67.9
list4.pop(2)
'hii'
list4
[100, 'hii', 'jerrry', True]
list2.clear()
list2
[]
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list1
[10, 2, 3, 4]
list3
[10, 2, 3, 4]
list3=list(list1)
id(list1)
1814410151232
id(list2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    id(list2)
NameError: name 'list2' is not defined. Did you mean: 'list1'?
id(list2)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    id(list2)
NameError: name 'list2' is not defined. Did you mean: 'list1'?
id(list3)
1814370072192
list3[2]=90
list1
[10, 2, 3, 4]
list3
[10, 2, 90, 4]
tuple1=(11, 21, 31, 41, 51)
tuple1
(11, 21, 31, 41, 51)
type(tuple1)
<class 'tuple'>
tuple1(3)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    tuple1(3)
TypeError: 'tuple' object is not callable
tuple1[3]
41
tuple1[3] = 44
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    tuple1[3] = 44
TypeError: 'tuple' object does not support item assignment
tuple1[0:4:2]
(11, 31)
tuple1.index(31)
2
tuple1.count(21)
1
id(tuple1)
1814367529728
tuple2 =  tuple 1
SyntaxError: invalid syntax
tuple2 =  tuple1
tuple2
(11, 21, 31, 41, 51)
id(tuple2)
1814367529728
tuple3=tuple(list1)
tuple3
(10, 2, 3, 4)
list1
[10, 2, 3, 4]
list1.append(tuple1)
list1[3]
4
>>> list1[4]
(11, 21, 31, 41, 51)
>>> list1[4][4]
51
>>> set1={12,34,56,78,90}
>>> set1
{34, 56, 90, 12, 78}
>>> set1[2]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
>>> set1.add(67)
>>> set1
{34, 67, 56, 90, 12, 78}
>>> set1.add('67')
>>> set1
{'67', 34, 67, 56, 90, 12, 78}
>>> set1.add(67)
>>> set1
{'67', 34, 67, 56, 90, 12, 78}
>>> set2=set(set1)
>>> set2
{'67', 34, 67, 56, 90, 12, 78}
>>> set1.union(set2)]
SyntaxError: unmatched ']'
>>> set1.union(set2)
{'67', 34, 67, 12, 78, 56, 90}

