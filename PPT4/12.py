#wap in python to find the second largest number in alist
original_list = input("Enter the elements of the list: ").split()
original_list = [int(item) for item in original_list]
largest = second_largest = float('-inf')
for num in original_list:
if num > largest:
second_largest = largest
largest = num
elif num > second_largest and num != largest:
second_largest = num
if second_largest == float('-inf'):
print("There is no second largest number.")
else:
print("Second largest number:", second_largest)
