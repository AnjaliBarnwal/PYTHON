#CHECK WHETHER SYMMETRICAL/PALINDROME STRING
input_string = input("Enter a string:")
is_palindrome = True
for i in range(len(input_string) // 2):
if input_string[i] != input_string[len(input_string) - 1 - i]:
  is_palindrome = False
break
if is_palindrome:
print("The string is a palindrome or symmetrical.")
else:
print("The string is not a palindrome or symmetrical.")
