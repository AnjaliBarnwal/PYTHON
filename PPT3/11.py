11. Write a program to input a list of numbers and sort using selection sort.
def selection_sort(arr):
for i in range(len(arr)):
min_index = i
for j in range(i+1, len(arr)):
if arr[j] < arr[min_index]:
min_index = j
arr[i], arr[min_index] = arr[min_index], arr[i]

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

selection_sort(arr)

print("Sorted list:", arr)
