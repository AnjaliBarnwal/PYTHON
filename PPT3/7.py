7.Write a program to input a number and search in a list using linear search.
def linear_search(arr, target):
for index, value in enumerate(arr):
if value == target:
return index
return -1

arr = [10, 20, 30, 40, 50, 60, 70]
target = int(input("Enter the number to search: "))

index = linear_search(arr, target)

if index != -1:
print(f"Number {target} found at index {index}")
else:
print(f"Number {target} not found in the list")
