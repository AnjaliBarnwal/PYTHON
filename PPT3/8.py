8. Write a program to input a number and search in a list using binary search.
def binary_search(arr, target):
left, right = 0, len(arr) - 1

while left <= right:
mid = (left + right) // 2

if arr[mid] == target:
return mid
elif arr[mid] < target:
left = mid + 1
else:
right = mid - 1

return -1

arr = [10, 20, 30, 40, 50, 60, 70]
target = int(input("Enter the number to search: "))

index = binary_search(arr, target)

if index != -1:
print(f"Number {target} found at index {index}")
else:

print(f"Number {target} not found in the list")
