12. Write a program to find the frequency of characters in a given string.
def char_frequency(string):
frequency = {}
for char in string:
if char in frequency:
frequency[char] += 1
else:
frequency[char] = 1
return frequency

string = input("Enter a string: ")

frequency = char_frequency(string)

for char, count in frequency.items():
print(f"Character '{char}' appears {count} times.")
