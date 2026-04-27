import re

# #beginning and end match code
#
# txt = input('Enter a text: ')
# beginPattern = input('Enter beginning pattern: ')
# endPattern = input('Enter ending pattern: ')
# beginPattern = '^' + beginPattern
# endPattern = endPattern + '$'
#
# if re.search(pattern=beginPattern, string=txt):
#     print('Beginning pattern available')
#
# else:
#     print('Beginning pattern not available')
#
# if re.search(pattern=endPattern, string=txt):
#     print('Ending pattern available')
#
# else:
#     print('Ending pattern not available')
#

#search method is used when you want that particular char
# , when it got caught it, skips all other elements

#digit
# full match checks every character matches the given pattern or not
#
# mbno = input('Enter your number: ')
#
# pat = r"[0-9]"
#
# if re.fullmatch(pattern=pat, string=mbno):
#     print('Only Digits')
# else:
#     print('Not only digits other characters also available')


#username

#match checks only the first 8 chars and return true but not
# the full string so put the start and end symbol..
# or else use fullmatch

# email

# + indicates one or more occurences
#. can be matched for any char except \n
#
# mailid = input('Enter your email id: ')
#
# pat = r"^[a-zA-z0-9_]+@[a-z]+\.[a-z]+$"
#
# if re.match(pattern=pat, string=mailid):
#     print('Valid')
# else:
#     print('Invalid')
#
#

#password

# ?= do search the specified pattern anywhere

# pwd = input('Enter your password to check whether it is strong or not: ')
#
# pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
#
# if re.match(pattern=pat, string=pwd):
#     print('Valid')
# else:
#     print('Invalid')
#


#substition removal of whitespaces

text = input('Text: ')

pat = r"\s+"

# print(re.sub(pattern=pat, string=text,repl=' '))
print(re.split(pattern=pat, string=text))
