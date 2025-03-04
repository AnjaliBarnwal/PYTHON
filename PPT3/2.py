2. Write a program to input a 10 digit number and find the digit with maximum value.
number = input("Enter a 10-digit number: ")
max_digit = number[0]
for digit in number:

if digit > max_digit:
max_digit = digit
print("The digit with the maximum value is:", max_digit)
