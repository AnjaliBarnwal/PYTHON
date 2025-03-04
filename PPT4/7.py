#to replace all characters of a list except the given character
input_string=input("Enter a string:")
char_to_keep = input("Enter the character to keep: ")
char_list = list(input_string)
for i in range(len(char_list)):
if char_list[i] != char_to_keep:
char_list[i] = ""
result = "".join(char_list)
print("Modified string:", result
