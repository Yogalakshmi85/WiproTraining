Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = 'jerry'
type(s1)
<class 'str'>
s1.capitalize()
'Jerry'
s1.casefold()
'jerry'
s1.center()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s1.center()
TypeError: center expected at least 1 argument, got 0
s1.upper()
'JERRY'
s1.endswith(y)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s1.endswith(y)
NameError: name 'y' is not defined
s1.endswith('y')
True
s1.count()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1.count()
TypeError: count expected at least 1 argument, got 0
KeyboardInterrupt
s1.count('r')
2
s1.find('r')
2
s1.find('o')
-1
s1.index('j')
0
s1.index('y')
4
s1.index('m')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1.index('m')
ValueError: substring not found
s1.isalpha()
True
s1.isascii()
True
s1.join('TOM')
'TjerryOjerryM'
s1.replace('y','i')
'jerri'
'jerri'
'jerri'
s2='TOM AND JERRY'
s2,split('E')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s2,split('E')
NameError: name 'split' is not defined
s2.split('E')
['TOM AND J', 'RRY']
s2.split(' ')
['TOM', 'AND', 'JERRY']
s2.swapcase()
'tom and jerry'
>>> s2.len()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s2.len()
AttributeError: 'str' object has no attribute 'len'
>>> len(s1)
5
>>> len(s2)
13
>>> s2.[9]
SyntaxError: invalid syntax
>>> s2[9]
'E'
>>> s2[-9]
'A'
>>> s2[0:9]
'TOM AND J'
>>> s2[0:]
'TOM AND JERRY'
>>> s2[1:12:3]
'OA R'
>>> s2[:]
'TOM AND JERRY'
>>> s2[::4]
'TAJY'
>>> s2[-8:-12]
''
>>> s2[-12:-8]
'OM A'
