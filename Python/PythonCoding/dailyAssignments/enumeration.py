text= input("Enter any text:")

count = 0

for i, char in enumerate(text):
    if char == 'a':
        count += 1

print("Number of 'a' in the given text is ", count)