#print even length words in a string
input_string = input("Enter a string: ")
words = input_string.split()
for word in words:
if len(word) % 2 == 0: # If the length of the word is even
print(word)
