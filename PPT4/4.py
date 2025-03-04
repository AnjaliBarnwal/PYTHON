#remove ith character from the string
input_string = input("Enter a string: ")
i = int(input("Enter the index of the character to remove: "))
result = ""
for index in range(len(input_string)):
if index != i:
result += input_string[index]
print("String after removing the character:", result)
