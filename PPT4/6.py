#check anagram string
string1 =input("Enter the first string: ")
string2 = input("Enter the second string: ")
if len(string1) != len(string2):
print("The strings are not anagrams.")
else:
sorted_string1 = ""
sorted_string2 = ""
while len(string1) > 0:
min_char = string1[0]
for char in string1:
if char < min_char:
min_char = char
sorted_string1 += min_char
string1 = string1.replace(min_char, "", 1)
while len(string2) > 0:
min_char = string2[0]
for char in string2:
if char < min_char:
min_char = char
sorted_string2 += min_char
string2 = string2.replace(min_char, "", 1)
if sorted_string1 == sorted_string2:
print("The strings are anagrams.")
else:
print("The strings are not anagrams.")
