#removing all duplicates from a string in python
string = input("Enter a string: ")
result = ""
for char in string:
if char not in result:
result += char
print("String after removing duplicates:", result)
