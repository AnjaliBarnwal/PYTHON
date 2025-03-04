6. Given a sorted array of positive integers arr, and an integer n which represents the length of arr, the
task is to rearrange the array elements alternatively i.e first element should be max value, second
should be min value, third should be second max, fourth should be second min and so on.
def rearrange(arr, n):
result = [0] * n
left, right = 0, n - 1

for i in range(n):
if i % 2 == 0:
result[i] = arr[right]
right -= 1
else:
result[i] = arr[left]
left += 1

return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)

rearranged_array = rearrange(arr, n)
print(rearranged_array)

