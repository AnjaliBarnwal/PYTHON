9. Write a program to input a list of numbers and sort using bubble sort.
def bubble_sort(arr):
n = len(arr)
for i in range(n):
swapped = False
for j in range(0, n-i-1):
if arr[j] > arr[j+1]:
arr[j], arr[j+1] = arr[j+1], arr[j]
swapped = True
if not swapped:
break

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

bubble_sort(arr)

print("Sorted list:", arr)
