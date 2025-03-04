13. Write a program to input a string and a number to encode the string by adding the number to every
character in the string
def encode_string(string, num):
encoded = ""
for char in string:
encoded += chr(ord(char) + num)
return encoded

string = input("Enter a string: ")
num = int(input("Enter a number to encode the string: "))

encoded_string = encode_string(string, num)

print("Encoded string:", encoded_string)

