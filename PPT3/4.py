4. Write a program, which will find all such numbers between 1000 and 3000 such that each
digit of the number is an even number.
for number in range(1000, 3001):
if all(int(digit) % 2 == 0 for digit in str(number)):
print(number)

