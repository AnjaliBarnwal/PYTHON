#reverse words in string
input_string = input("Enter a string: ")
words = input_string.split()
reversed_string = ""
for i in range(len(words) - 1, -1, -1):
reversed_string += words[i] + " "
print("Reversed string:", reversed_string[:-1])
